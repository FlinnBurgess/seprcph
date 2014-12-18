doxygen
git checkout gh-pages doxygen/html
git pull origin gh-pages
git add -f doxygen/html
git commit -a -m "Updated docs"
