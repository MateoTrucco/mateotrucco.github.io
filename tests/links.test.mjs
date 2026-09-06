import assert from "node:assert/strict";
import fs from "node:fs";
import { PROJECTS } from "../static/js/projects.js";

const html = fs.readFileSync(new URL("../index.html", import.meta.url), "utf8");
assert.equal(PROJECTS.length, 9);
assert.equal(
  new Set(PROJECTS.map((project) => project.slug)).size,
  PROJECTS.length,
);
assert.ok(html.includes('id="projectGrid"'));
assert.ok(html.includes('id="featuredProjects"'));
for (const project of PROJECTS) {
  assert.ok(
    project.title &&
      project.description.en &&
      project.description.es &&
      project.proof.en &&
      project.proof.es,
    `incomplete bilingual metadata: ${project.slug}`,
  );
  assert.ok(
    ["python", "web", "systems", "data"].includes(project.category),
    `invalid category: ${project.slug}`,
  );
  assert.ok(project.visual, `missing symbolic visual: ${project.slug}`);
}
console.log(`Portfolio metadata verified for ${PROJECTS.length} projects.`);
