import { chromium } from "playwright";
import { fileURLToPath } from "url";
import path from "path";

const root = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(root, "..", "img", "posters", "exports");

const posters = [
  { file: "all-services.html", name: "fly-aero-poster-all-services.png", selector: ".poster-canvas--portrait" },
  { file: "umrah.html", name: "fly-aero-poster-umrah.png", selector: ".poster-canvas--portrait" },
  { file: "uae-kerala.html", name: "fly-aero-poster-uae-kerala.png", selector: ".poster-canvas--portrait" },
  { file: "visa-passport.html", name: "fly-aero-poster-visa.png", selector: ".poster-canvas--portrait" },
  { file: "holiday-hotel.html", name: "fly-aero-poster-holiday.png", selector: ".poster-canvas--portrait" },
  { file: "instagram-square.html", name: "fly-aero-poster-instagram.png", selector: ".poster-canvas--square" },
  { file: "story.html", name: "fly-aero-poster-story.png", selector: ".poster-canvas--story" },
];

const browser = await chromium.launch();
const page = await browser.newPage({ deviceScaleFactor: 2 });

for (const p of posters) {
  const url = "file://" + path.join(root, p.file);
  await page.goto(url, { waitUntil: "networkidle" });
  await page.waitForTimeout(800);
  const el = page.locator(p.selector);
  await el.screenshot({ path: path.join(outDir, p.name) });
  console.log("wrote", p.name);
}

await browser.close();
