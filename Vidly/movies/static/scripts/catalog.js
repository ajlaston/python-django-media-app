var movieCat = $('#movies');
var seriesCat = $('#series');


displayMovie = (movie) => {
    
    movieCat.append(`<li class="card card-style"><h5 class="card-title">${movie.title}</h5> 
    <b>Year:</b> ${movie.release_year}<br> <b>Length:</b> ${movie.duration_min} min <p class="card-text" >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Assumenda
     ratione vero consectetur architecto officia.</p> <button class="btn btn-primary">Read More</button></li>`);
}

getData = () => {
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success : function(res){
            let movies = res.objects;
            movies.forEach(element => {
                displayMovie(element);
            });
        },
        error : function(details){
            console.log('Error', details)
        }
    });
}


init = ()=>{
    console.log('Hello World');
    getData();
}

window.onload = init();


