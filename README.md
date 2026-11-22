# JuliaPagekit

A lightweight, Python-based static site generator that turns `.jhtml` files into HTML pages using custom templates.

> [!WARNING]
> **JuliaPagekit is in very early development.**
>
> This project is in alpha experimental and incomplete. Features may be missing, documentation may be outdated, and things may change or break without notice. Cation is advised.

## Features

- **Page files:** Write pages in `.jhtml` files using HTML and custom page metadata.
- **Templates:** Use custom HTML templates with inheritance, variables and nested templates (one level of nesting).
- **Configuration:** Configure the generator using `.jconf` files.
- **Directory structure:** Automatically scan content directories and preserve their structure in the generated website.
- **Static assets:** Copy files such as images, fonts, CSS and JavaScript into the output directory.
- **HTML output:** Generate static HTML files, with basic HTML minification.
- **Generated files:** Automatically create `robots.txt` and `security.txt`.
- **Email and text protection:** hide emails or select text blocks until javascript is executed in the browser (Important: text and email are not encrypted just base64 encoded in the source code and not displayed, this is only ment to complicate automated scraping)

## Planned Features

- Automatic navigation and breadcrumb generation.
- Optional blog functionality.
- Real automatic generation of `security.txt`.

## Non-Goals

JuliaPagekit is intentionally kept small and focused. The following are outside its scope:

- **Additional content formats:** No Markdown, MDX, reStructuredText or other input formats. Pages are written in `.jhtml`.
- **Content management:** No CMS, visual editor, user management or publishing workflow.
- **Dynamic functionality:** No server-side execution, database integration, authentication or API backend.
- **Extensibility framework:** No plugin system, lifecycle hooks or custom processing pipelines.
- **Hosting and deployment:** JuliaPagekit only generates static files. Hosting and deployment are handled separately (for example with GitHub Pages).

## About the Name

The name **JuliaPagekit** combines my name, *Julia*, with *Pagekit*, reflecting the project's purpose.

JuliaPagekit is being developed primarily with the primary goal of building my own personal website as part of an upcoming rebuild. What started as a tool for a personal project is intended to become a standalone static site generator that others can use as well.

The name reflects both the personal motivation behind the project and its goal of allowing easy creation of fully custom websites.

## How to use
!TODO: Add how to user

## Contributing

Contributions, suggestions and bug reports are welcome. If you would like to contribute, please contact me by email.
