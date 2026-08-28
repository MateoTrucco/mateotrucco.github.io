import assert from 'node:assert/strict';
import fs from 'node:fs';
import { PROJECTS } from '../static/js/projects.js';

const html = fs.readFileSync('index.html', 'utf8');
assert.equal(PROJECTS.length, 15);
assert.equal(new Set(PROJECTS.map((project) => project.slug)).size, PROJECTS.length);
assert.ok(html.includes('id="projectGrid"'));
assert.ok(html.includes('id="featuredProjects"'));
for (const project of PROJECTS) {
  assert.ok(project.title && project.description && project.proof, `incomplete project metadata: ${project.slug}`);
  assert.ok(['python', 'web', 'systems'].includes(project.category), `invalid category: ${project.slug}`);
}
console.log(`Portfolio metadata verified for ${PROJECTS.length} projects.`);
