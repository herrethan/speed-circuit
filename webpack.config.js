// const glob = require('glob');
const path = require('path');
// const webpack = require('webpack');
// const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = [];

// bundle sass -> css
module.exports.push({
  entry: './app/static/scss/base.scss',
  output: {
    // This is necessary for webpack to compile
    // But we never use style-bundle.js
    filename: 'style-bundle.js',
  },
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        {
          loader: 'file-loader',
          options: {
            name: './app/static/dist/style.css',
          },
        },
        { loader: 'extract-loader' },
        { loader: 'css-loader' },
        {
          loader: 'sass-loader',
          options: {
            importer: function(url, prev) {
              if(url.indexOf('@material') === 0) {
                var filePath = url.split('@material')[1];
                var nodeModulePath = `./node_modules/@material/${filePath}`;
                return { file: path.resolve(nodeModulePath) };
              }
              return { file: url };
            }
          }
        }
      ]
    }]
  },
});

// bundle jsx -> js
module.exports.push({
  entry: "./app/static/js/index.jsx",
  output: {
    filename: "./app/static/dist/bundle.js"
  },
  module: {
    loaders: [{
      test: /\.jsx$/,
      loader: 'babel-loader',
      query: {
        presets: ['es2015']
      }
    }]
  },
});

// const config = {
//   entry:  __dirname + '/app/static/js/index.jsx',
//   output: {
//       path: __dirname + '/app/static/dist',
//       filename: 'bundle.js',
//   },
//   // resolve: {
//   //     extensions: ['.js', '.jsx', '.css']
//   // },
//   module: {
//     rules: [
//       {
//         test: /\.jsx?/,
//         exclude: /node_modules/,
//         use: 'babel-loader'
//       },
//       {
//         test: /\.scss$/,
//         use: ExtractTextPlugin.extract({
//           fallback: 'style-loader',
//           use: [
//             {
//               loader: 'css-loader'
//             },
//             {
//               loader: 'sass-loader',
//               options: {
//                 importer: function(url, prev) {
//                   if(url.indexOf('@material') === 0) {
//                     var filePath = url.split('@material')[1];
//                     var nodeModulePath = `./node_modules/@material/${filePath}`;
//                     return { file: path.resolve(nodeModulePath) };
//                   };
//                   // if(url.indexOf('material-components-web/') === 0) {
//                   //   var nodeModulePath = `./node_modules/material-components-web/material-components-web`;
//                   //   return { file: path.resolve(nodeModulePath) };
//                   // }
//                   return { file: url };
//                 }
//               }
//             }
//           ]
//         })
//       }
//     ]
//   },
//   plugins: [
//     new ExtractTextPlugin('style.css')
//   ]
// };

// module.exports = config;
