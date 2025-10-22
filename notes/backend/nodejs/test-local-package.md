---
title: "Test local package"
description: "How to test local npm packages using link: protocol or npm install with local path"
tags: [nodejs, npm, local-development, testing, packages]
---
package.json
```json
"dependencies": {
	"code2image": "link:../code2image/dist",
}
```

or 
npm install /path-to-local-package
