const path = require('path')



module.exports = {
    entry: {
        base: './static/javascript/base.js',
        home: './static/javascript/home/home.js',
        fliers: './static/javascript/media/fliers.js',
        photos: './static/javascript/media/photos.js',
        videos: './static/javascript/media/videos.js',
        list_genres: './static/javascript/music/list_genres.js',
        view_genre: './static/javascript/music/view_genre.js',
        music_page: './static/javascript/music/music_page.js',
        view_artist: './static/javascript/music/view_artist.js',
        past_shows: './static/javascript/shows/past_shows.js',
        view_show: './static/javascript/shows/view_show.js',
        form_to_bootstrap: './static/javascript/util/form_to_bootstrap.js'
    },
    output: {
        path: path.join(__dirname,'static', 'dist'),
        publicPath: '/',
        filename: '[name].js',
        library: 'scripts'
    },
    target: 'web',

    module: {
        rules: [
            {
                // Transpiles ES6-8 into ES5
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}