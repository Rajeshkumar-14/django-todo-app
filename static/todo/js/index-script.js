$(document).ready(function () {
    // Function to apply styles based on theme START ---------->
    function applyThemeStyles(preferredDarkMode) {
        var themeText = $('.navbar-theme-text');
        var themeIcon = $('.navbar-theme-icon');
        if (preferredDarkMode) {
            // Dark Mode
            themeText.text('Dark Theme');
            themeIcon.removeClass('fa-lightbulb fa-sun').addClass('fa-moon');
            $('body').removeClass('text-dark bg-light').addClass('bg-dark text-white');
            $('.card').removeClass('text-dark bg-light').addClass('text-white bg-dark');
            $('.navbar').addClass('border-bottom navbar-dark bg-dark').removeClass('navbar-light bg-light border-dark');
            $('.task-display-table').addClass('table-dark').removeClass('table-light');
            $('.view-task-table').addClass('table-dark').removeClass('table-light');
            $('.modal-content').addClass('bg-dark text-white').removeClass('bg-light text-dark');

        } else {
            // Light Mode   
            themeText.text('Light Theme');
            themeIcon.removeClass('fa-moon').addClass('fa-lightbulb fa-sun');
            $('body').removeClass('bg-dark text-white').addClass('text-dark bg-light');
            $('.card').removeClass('text-white bg-dark').addClass('text-dark bg-light');
            $('.navbar').removeClass('navbar-dark bg-dark').addClass('border-bottom bg-light navbar-light border-black');
            $('.task-display-table').removeClass('table-dark').addClass('table-light');
            $('.view-task-table').removeClass('table-dark').addClass('table-light');
            $('.modal-content').removeClass('bg-dark text-white').addClass('bg-light text-dark');
        }
    }
    // Function to get user's system default theme
    function getUserSystemTheme() {
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    }

    // Apply theme styles on page load
    applyThemeStyles(getUserSystemTheme());

    // Theme toggle click events
    $('.toggle-light').click(function () {
        applyThemeStyles(false);
    });

    $('.toggle-dark').click(function () {
        applyThemeStyles(true);
    });

    $('.toggle-default').click(function () {
        applyThemeStyles(getUserSystemTheme());
    });
    // Function to apply styles based on theme END ---------->
});
