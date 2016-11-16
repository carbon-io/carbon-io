$(document).ready(function () {
    var header_height = $('header#mlab-header').height();

    function scroll_to_id(id) {
        var elem = $(id);
        if (elem) {
            $('html, body').scrollTop(elem.offset().top - header_height - 20);
        }
    }

    // Override default action on link elements when the href is an anchor.
    // Avoid the hashchange event altogether, as it will flicker -- scroll to
    // where the browser thinks we should be first, then our real position via
    // the call to scroll_to_id
    $('a').on('click', function (event) {
        if (this.hash && this.hash.startsWith('#')) {
            if (history.pushState) {
                history.pushState(null, null, this.hash);
                scroll_to_id(this.hash);
            }
            else {
                location.hash = this.hash;
            }
            event.preventDefault();
        }
    });

    // Triger after timeout because we can't prevent the default action of a
    // hashchange on page load
    $(window).on('hashchange', function () {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    });

    // Initial trigger, if there is a hash in the URL
    if (window.location.hash) {
        setTimeout(function () { scroll_to_id(window.location.hash) }, 25);
    }

    // Mobile menu
    $('header#mlab-header div.mobile-menu a').on('click', function(event) {
        $('header#mlab-header').toggleClass('shift');
        event.preventDefault();
    })

    // Override scrolling from theme
    SphinxRtdTheme.StickyNav.onScroll = function () {};
});
