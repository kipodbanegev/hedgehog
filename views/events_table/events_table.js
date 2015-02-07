$(function() {
    $(".events_table .btn").click(function() {
	$(".events_table .btn").removeClass('active');
	$(this).addClass('active');
    });
});