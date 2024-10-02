const listen = (opts, handler) => {
  const http = require('http')
  const getRawBody = require('raw-body')

  const port = process.env.PORT
  http.createServer(async (req, res) => {
    if (opts.subscribe && req.method !== 'POST') {
      res.writeHead(405).end()
      return
    }
    let reqBody
    if (req.method !== 'GET') {
      try {
        reqBody = await getRawBody(req, {
          length: req.headers['content-length'],
          limit: '20kb',
          encoding: 'utf8',
        })
      } catch {
        res.writeHead(413).end()
        return
      }
    }
    if (opts.subscribe) {
      if (req.method !== 'POST') {
        res.writeHead(405).end()
        return
      }
      if (req.headers.origin !== undefined) {
        res.writeHead(403).end()
        return
      }
      const data = JSON.parse(reqBody).message.data
      await handler({
        message: JSON.parse(Buffer.from(data, 'base64').toString()),
      })
      res.writeHead(204).end()
    } else {
      const idx = req.url.indexOf('?')
      let pathname
      let query
      if (idx === -1) {
        pathname = req.url
        query = {}
      } else {
        pathname = req.url.slice(0, idx)
        query = Object.fromEntries(new URLSearchParams(req.url.slice(idx)))
      }
      const { statusCode, headers, body } = await handler({
        pathname,
        query,
        method: req.method,
        headers: req.headers,
        body: reqBody,
      })
      res.writeHead(statusCode, headers).end(body)
    }
  }).listen(port, () => {
    console.log('listening on', port)
  })
}

if (process.env.AWS_EXECUTION_ENV) {
  exports.runtime = 'aws'

  const ric = require('aws-lambda-ric')
  const { SQS } = require('@aws-sdk/client-sqs')

  const sqs = new SQS()

  const runSubscribe = (opts, handler) => {
    for (let i = 0; i < 5; i++) {
      ;(async () => {
        while (true) {
          let msg
          let body
          try {
            const { Messages } = await sqs.receiveMessage({
              QueueUrl: process.env.APP_SQS_URL,
              WaitTimeSeconds: 20
            })
            if (!Messages) {
              continue
            }
            msg = Messages[0]
            body = JSON.parse(Buffer.from(msg.Body, 'base64').toString())
          } catch (e) {
            console.error(e)
            continue
          }
          await handler({ message: body })
          await sqs.deleteMessage({
            QueueUrl: process.env.APP_SQS_URL,
            ReceiptHandle: msg.ReceiptHandle,
          })
        }
      })()
    }
  }

  const runHttp = (opts, handler) => {
    exports._ricHandler = async (evt) => {
      let body
      if (evt.method !== 'GET') {
        body = evt.isBase64Encoded
          ? Buffer.from(evt.body, 'base64').toString()
          : evt.body
      }
      const query = Object.fromEntries(Object.entries(evt.queryStringParameters)
        .map(entry => [entry[0], decodeURIComponent(entry[1])]))
      return handler({
        pathname: evt.path,
        query,
        method: evt.httpMethod,
        headers: evt.headers,
        body,
      })
    }
    ric.run('.', 'server._ricHandler')
  }

  exports.run = (opts, handler) => {
    if (opts.subscribe) {
      runSubscribe(opts, handler)
    } else {
      runHttp(opts, handler)
    }
  }
  exports.publish = message => sqs.sendMessage({
    MessageBody: Buffer.from(JSON.stringify(message)).toString('base64'),
    QueueUrl: process.env.APP_SQS_URL,
  })
} else if (process.env.K_SERVICE) {
  exports.runtime = 'gcp'

  exports.run = listen

  if (process.env.APP_PUBSUB_TOPIC) {
    const { PubSub } = require('@google-cloud/pubsub')
    const topic = new PubSub().topic(process.env.APP_PUBSUB_TOPIC)
    exports.publish = message => topic.publishMessage({ json: message })
  }
} else {
  exports.runtime = 'local'

  const http = require('http')

  exports.run = listen

  exports.publish = (message) => {
    const req = http.request('http://localhost:8081', { method: 'POST' })
    req.end(JSON.stringify({
      message: {
        data: Buffer.from(JSON.stringify(message)).toString('base64'),
      },
    }))
  }
}
