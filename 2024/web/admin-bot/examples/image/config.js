const sleep = time => new Promise(resolve => setTimeout(resolve, time))

const challenges = new Map([
  ['one', {
    name: 'Challenge One',
    timeout: 10000,
    handler: async (url, ctx) => {
      const page = await ctx.newPage()
      await page.setCookie({ name: 'flag', value: 'flag{abcd}', url })
      await page.goto(url, { timeout: 3000, waitUntil: 'domcontentloaded' })
      await sleep(5000)
    }
  }]
])

module.exports = {
  challenges
}
