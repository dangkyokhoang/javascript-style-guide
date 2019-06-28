'use strict';

const fs = require('fs');

const readme = fs.readFileSync('README.md', 'utf8');
const terminology = fs.readFileSync('terminology.md', 'utf8');
const back = '**[⬆ về đầu trang](#table-of-contents)**';

// Terminology section is to be inserted before the translation section
const search = /\s+(##.+"terminology"[\s\S]+|)(?=##.+"translation")/;
const replacement = `\n\n${terminology.trim()}\n\n${back}\n\n`;

fs.writeFileSync('README.md', readme.replace(search, replacement));
