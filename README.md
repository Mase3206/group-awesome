# A Guide to The Galaxy

A self-paced space tour app.

## Requirements

- Python 3.12 or newer
- Node.js (only required during development)

## Start development

```shell
# clone this repo
git clone https://github.com/Mase3206/group-awesome

# prepare environment
python -m venv venv

# install requirements
python -m pip -r requirements.txt
npm install # installs to the node_modules folder

# run the dev server
python manage.py runserver
```

### Extra commands

If you are making edits to the styling of the page, you'll likely want to run `npm run-script compile-sass:watch` alongside `manage.py runserver` as you do so. This runs the Sass compiler and tells it to watch for changes in the style directory, re-compiling the source Sass files when a change occurs. 
```shell
npm run-script compile-sass:watch
```

If you are editing the custom theme of the Allauth screens, you will need to run `npm run-script build-allauth` after each edit (or `build-allauth:watch` to watch for changes).
```shell
npm run-script build-allauth
```

If you just want to quickly build and compile everything, run `npm run-script build`. This will compile the Sass stylesheets, build the Allauth themes, and run `manage.py collectstatic --noinput`. 
```shell
npm run-script build
```

## Deployment Notes

- Make sure you have the latest version of the secrets.yml file. This is intentionally not committed to the repository, so you'll need to get it from a contributor.
- Before deploying, run `npm run-script build` to ensure the server gets the latest versions of the stylesheets.
