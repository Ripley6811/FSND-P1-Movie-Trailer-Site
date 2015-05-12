// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $('#trailer-video-container').empty();
});

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    // Close modal and skip Youtube loading if website link button is clicked.
    if ($(event.target).hasClass('btn')) {
        $('#trailer').modal('hide');
        return;
    }
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $('#trailer-video-container').empty().append($('<iframe></iframe>', {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
});

// Animate the movie tiles when the page loads
$(document).ready(function () {
    $('.movie-tile').hide().first().show('fast', function showNext() {
        $(this).next('div').show('fast', showNext);
    });
});