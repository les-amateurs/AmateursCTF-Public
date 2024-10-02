const sleep = time => new Promise(resolve => setTimeout(resolve, time))

const challenges = new Map([
  ['busy-bee', {
    name: 'Busy Bee',
    timeout: 10000,
    handler: async (url, ctx) => {
      const page = await ctx.newPage()
      page.on("console", async (msg) => {
        const msgArgs = msg.args();
        for (let i = 0; i < msgArgs.length; ++i) {
          console.log(await msgArgs[i].jsonValue());
        }
      });
      console.log(await page.browser().version());
      await page.goto("https://busy-bee-amateurs-ctf-2024.pages.dev/", { timeout: 3000, waitUntil: 'domcontentloaded' })
      await page.evaluate(() => {
        localStorage.setItem("flag", "amateursCTF{th3_m0ther_b33_i5_HAPPY}")
      })
      await page.goto("about:blank", {
        timeout: 3000,
        waitUntil: "domcontentloaded",
      });
      console.log("going to " + url)
      await page.goto(url, { timeout: 3000, waitUntil: 'domcontentloaded' })
      await sleep(2000)
      console.log("clicking play")
      await page.evaluate(() => {
        console.log("hopes and dreams: " + !!window.Sanitizer);
        document.querySelector("#controls :first-child").click();
      })

      await sleep(5000)
      await page.evaluate(() => {
        console.log(document.location.href);
      })
      await sleep(1000);
    },
    urlRegex: /^https:\/\/busy-bee-amateurs-ctf-2024\.pages\.dev/,
  }],
  ['sculpture', {
    name: 'sculpture',
    timeout: 10000,
    handler: async (url, ctx) => {
      const page = await ctx.newPage()
      console.log(await page.browser().version());
      await page.goto("https://amateurs-ctf-2024-sculpture-challenge.pages.dev/?ref=adminb0t", { timeout: 3000, waitUntil: 'domcontentloaded' })
      await sleep(1000);
      await page.evaluate(() => {
        localStorage.setItem("flag", "amateursCTF{i_l0v3_wh3n_y0u_can_imp0rt_xss_v3ct0r}")
      })
      await sleep(1000);
      console.log("going to " + url)
      await page.goto(url, { timeout: 3000, waitUntil: 'domcontentloaded' })
      await sleep(1000)
    },
    urlRegex: /^https:\/\/amateurs-ctf-2024-sculpture-challenge\.pages\.dev/,
  }]
])

module.exports = {
  challenges
}
