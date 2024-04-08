# Dynamic Tree-Structured Menu for Django

Developed for Uptrader, this Django app introduces a dynamic, tree-structured menu system, designed to enhance navigation and user experience within any Django project.

## Features

- **Template Tag Integration**: Seamlessly integrates with Django templates for easy deployment.
- **Smart Expansion**: Automatically expands to show all items above and the first level below the currently selected item.
- **Database-Driven**: Fully manageable via the Django admin interface, allowing for real-time updates to the menu structure.
- **URL Awareness**: Dynamically highlights the active menu item based on the current page's URL.
- **Multipurpose Menus**: Supports multiple menus on a single page, identified by unique names.
- **Optimized Performance**: Engineered to render each menu with just one database query.

## Quick Start

Embed any named menu into your template with:

```django
{% draw_menu 'main_menu' %}
