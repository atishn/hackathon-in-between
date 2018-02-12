// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var autoprefixer = require('gulp-autoprefixer');
var babel = require('gulp-babel');
var concat = require('gulp-concat');
var jshint = require('gulp-jshint');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var uglify = require('gulp-uglify');

// Lint Task
gulp.task('lint', function() {
  return gulp.src('_assets/js/src/*.js')
    .pipe(babel({
      presets: ['env']
    }))
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

// Compile Sass
gulp.task('sass', function() {
  return gulp.src('_assets/scss/*.scss')
    .pipe(sass({ style: 'compressed' }))
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(minifycss())
    .pipe(gulp.dest('.'));
});

// Concatenate JS Plugins
gulp.task('plugins', function() {
  return gulp.src('node_modules/material-components-web/dist/material-components-web.js')
    .pipe(concat('plugins.js'))
    .pipe(gulp.dest('_assets/js/build'));
});

// Concatenate & Minify JS
gulp.task('scripts', function() {
  return gulp.src('_assets/js/src/*.js')
    .pipe(babel({
      presets: ['env']
    }))
    .pipe(concat('app.js'))
    .pipe(gulp.dest('_assets/js/build'))
    .pipe(rename('app.min.js'))
    .pipe(gulp.dest('_assets/js/build'));
});

// Watch Files For Changes
gulp.task('watch', function() {
  gulp.watch(['_assets/js/src/*.js'], [ /*'lint',*/ 'plugins', 'scripts' ]);
  gulp.watch(['_assets/scss/*.scss','_assets/scss/**/*.scss'], ['sass']);
});

// Default Task
gulp.task('default', [ /*'lint',*/ 'sass', 'plugins', 'scripts', 'watch' ]);
