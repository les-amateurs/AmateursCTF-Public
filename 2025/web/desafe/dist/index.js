import { serve } from '@hono/node-server'
import { Hono } from 'hono'
import { readFileSync } from 'fs'
import * as devalue from 'devalue';

const app = new Hono()
const FLAG = readFileSync('flag.txt')

class FlagRequest {
  constructor(feedback) {
    // your feedback is greatly appreciated!
    delete { feedback }
  }

  get flag() {
    if (this.admin) {
      return FLAG;
    } else {
      return "haha nope"
    }
  }
}

app.get('/', (c) => {
  return c.text(`POST /
Body: FlagRequest(feedback), must be devalue stringified`)
})

app.post('/', async (c) => {
  const body = await c.req.text();

  const flagRequest = devalue.parse(body, {
    FlagRequest: ([a]) => new FlagRequest(a),
  })


  if (!(flagRequest instanceof FlagRequest)) return c.text('not a flag request')

  return c.text(flagRequest.flag)
})

serve({
  fetch: app.fetch,
  port: 3000
}, (info) => {
  console.log(`Server is running on http://localhost:${info.port}`)
})
