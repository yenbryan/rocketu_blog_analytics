$(document).ready(function() {
    $("#featuredBlog").click(function () {
        mixpanel.track("Blog Footer Clicked");
    });
});