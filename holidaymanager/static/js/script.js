$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}});
    $('.modal').modal();
    $('select').formSelect();
});