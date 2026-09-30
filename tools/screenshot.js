// Takes screenshots of the site so changes can be previewed without deploying.
// Usage: node tools/screenshot.js [page.html] [selector]
//   node tools/screenshot.js                      -> full index.html
//   node tools/screenshot.js faq.html             -> full faq.html
//   node tools/screenshot.js index.html footer    -> just the footer
// Saves desktop and mobile PNGs to screenshots/ (not committed).
const path = require("path");
const fs = require("fs");
const { chromium } = require(require.resolve("playwright", { paths: [require("child_process").execSync("npm root -g").toString().trim()] }));

(async () => {
  const [pageName = "index.html", selector] = process.argv.slice(2);
  const root = path.resolve(__dirname, "..");
  const outDir = path.join(root, "screenshots");
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const base = pageName.replace(/\.html$/, "") + (selector ? "-" + selector.replace(/[^a-z0-9]+/gi, "") : "");
  for (const [label, width] of [["desktop", 1280], ["mobile", 390]]) {
    const page = await browser.newPage({ viewport: { width, height: 900 } });
    await page.goto("file://" + path.join(root, pageName));
    await page.evaluate(() => document.querySelectorAll(".fade").forEach((el) => el.classList.remove("waiting")));
    await page.waitForTimeout(300);
    const file = path.join(outDir, `${base}-${label}.png`);
    if (selector) await page.locator(selector).first().screenshot({ path: file });
    else await page.screenshot({ path: file, fullPage: true });
    console.log(file);
    await page.close();
  }
  await browser.close();
})();
