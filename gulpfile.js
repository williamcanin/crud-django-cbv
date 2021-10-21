const { src, dest, parallel, series, watch } = require('gulp')
const concat = require('gulp-concat')
const cssnano = require ('cssnano')
const plumber = require('gulp-plumber')
const postcss = require('gulp-postcss')
const rename = require('gulp-rename')
const sass = require('gulp-sass')(require('sass'))
const del = require('del')
const uglify = require('gulp-uglify-es').default
const browserSync = require('browser-sync').create()
const spawn = require('child_process').spawn
const reload = browserSync.reload

function pathsConfig(AppName, vendorsRoot) {
  return {
    vendorsJs: [
      `${vendorsRoot}/jquery/dist/jquery.js`,
      `${vendorsRoot}/jquery-mask-plugin/dist/jquery.mask.js`,
      // `${vendorsRoot}/bootstrap/dist/js/bootstrap.js`,
      `${vendorsRoot}/bootstrap/dist/js/bootstrap.bundle.min.js`,
    ],
    vendorsCss: [
      `${vendorsRoot}/@fortawesome/fontawesome-free/css/all.css`,
      `${vendorsRoot}/bootstrap/dist/css/bootstrap.css`,
    ],
    vendorsFonts: [
      `${vendorsRoot}/@fortawesome/fontawesome-free/webfonts/*`,
    ],
    clean: [
      `htmlcov`,
      `${AppName}/staticfiles`,
      `${AppName}/static/css`,
      `${AppName}/static/js`,
      `${AppName}/static/webfonts`,
      `${AppName}/static/images/*.png`,
      `${AppName}/static/images/*.jpg`,
    ],
    templates: `${AppName}/templates`,
    css: `${AppName}/static/css`,
    src: `${AppName}/static/src`,
    fonts: `${AppName}/static/webfonts`,
    js: `${AppName}/static/js`,
    env: `.env`,
  }
}

var paths = pathsConfig('management', 'node_modules')

var minifyCss = [
  cssnano({ preset: 'default' })   // minify result
]

function cleanObjs() {
  return del(paths.clean)
}

function vendorStyles() {
  return src(paths.vendorsCss)
    .pipe(concat('vendors.css'))
    .pipe(plumber()) // Checks for errors
    .pipe(rename({suffix: '.min'}))
    .pipe(postcss(minifyCss))
    .pipe(dest(paths.css))
}

function copyFonts() {
  return src(paths.vendorsFonts)
    .pipe(dest(paths.fonts))
}

function styles() {
  return src(`${paths.src}/sass/style.scss`)
  .pipe(sass({
    includePaths: [
      `${paths.src}/sass`
    ]
  }).on('error', sass.logError))
  .pipe(plumber()) // Checks for errors
  .pipe(dest(paths.css))
  .pipe(rename({ suffix: '.min' }))
  .pipe(postcss(minifyCss)) // Minifies the result
  .pipe(dest(paths.css))
}

function scripts() {
  return src(`${paths.src}/js/script.js`)
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.js))
}


function vendorScripts() {
  return src(paths.vendorsJs)
    .pipe(concat('vendors.js'))
    .pipe(dest(paths.js))
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.js))
}

function runServer(cb) {
  var cmd = spawn('poetry', ['run', 'python', 'manage.py', 'runserver'], {stdio: 'inherit'})
  cmd.on('close', function(code) {
    console.log('runServer exited with code ' + code)
    cb(code)
  })
}


function initBrowserSync() {
  browserSync.init(
    {
      files: [
        `${paths.css}/*.css`,
        `${paths.js}/*.js`,
        `${paths.templates}/**/*.html`
      ],
      port: 3000,
      notify: false,
      proxy: "127.0.0.1:8000",
    }
  )
}

function watchPaths() {
  watch(`${paths.env}`)
  watch(`${paths.src}/sass/**/*.scss`, styles)
  watch(`${paths.templates}/**/*.html`).on("change", reload)
  watch([`${paths.src}/js/**/*.js`, `!${paths.js}/*.min.js`], scripts).on("change", reload)
}

const generateAssets = parallel(
  styles,
  scripts,
  vendorScripts,
  vendorStyles,
  copyFonts,
)

const dev = parallel(
  runServer,
  initBrowserSync,
  watchPaths
)

const clean = parallel(cleanObjs)

exports.default = series(generateAssets, dev)
exports["assets"] = generateAssets
exports["dev"] = dev
exports["clean"] = clean
