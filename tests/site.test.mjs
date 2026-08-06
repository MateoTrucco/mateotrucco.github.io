import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
assert.match(html, /<title>Mateo Trucco/);
assert.match(html, /id="projects"/);
assert.doesNotMatch(html, /href="#"/);
for (const local of ['static/favicon.svg', 'static/css/styles.css', 'static/js/script.js']) {
  assert.ok(fs.existsSync(path.join(root, local)), `Missing ${local}`);
}
const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map((match) => match[1]);
assert.equal(new Set(ids).size, ids.length, 'HTML IDs must be unique');
console.log('Portfolio checks passed.');
