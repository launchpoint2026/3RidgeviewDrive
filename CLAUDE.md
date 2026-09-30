# 3 Ridgeview Drive website — working rules

One-page static site (`index.html` + `styles.css`) advertising the half-acre building lot at 3 Ridgeview Drive, Ross, CA 94957, for sale by owner.
Buyer contact is the owner's email, 3ridgeviewdrive@gmail.com (shown on the page on purpose). Price is "Email for price".

## After every change (always, without being asked)
1. Make the change.
2. Run `node tools/screenshot.js index.html [css-selector]`, look at the shots in `screenshots/`, and send them to the owner with SendUserFile (display: render).
3. Commit with a plain-English message and push straight to `main` (`git pull origin main && git push origin main`).
4. Reply in plain, non-technical language.
