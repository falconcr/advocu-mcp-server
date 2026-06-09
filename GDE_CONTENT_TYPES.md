# GDE Content Types - Valid Enum Values

## Valid contentType Values for GDE Content Creation

Based on the official Advocu API specification, the `contentType` field accepts the following 7 values:

1. **Articles** - Blog posts, written articles, tutorials
2. **Books** - Published books, eBooks
3. **Code contribution** - Open source contributions, code samples
4. **Demos** - Live demonstrations, proof of concepts
5. **Newsletters** - Newsletter content, regular publications
6. **Podcasts** - Audio podcast episodes
7. **Videos** - Video content, YouTube videos, screencasts

## Automatic Mapping

The `submit_gde_content` function now automatically maps common user inputs to these valid values:

```python
content_type_mapping = {
    "video": "Videos",
    "videos": "Videos",
    "youtube": "Videos",
    "article": "Articles",
    "articles": "Articles",
    "blog": "Articles",
    "blog post": "Articles",
    "book": "Books",
    "books": "Books",
    "code": "Code contribution",
    "code contribution": "Code contribution",
    "demo": "Demos",
    "demos": "Demos",
    "newsletter": "Newsletters",
    "newsletters": "Newsletters",
    "podcast": "Podcasts",
    "podcasts": "Podcasts",
}
```

## Usage Examples

### Correct Usage
```python
submit_gde_content(
    title="My Tutorial Video",
    content_type="video",  # Will be mapped to "Videos"
    date="2026-06-08",
    url="https://youtube.com/...",
    views=200
)
```

### Direct Enum Value
```python
submit_gde_content(
    title="My Tutorial Video",
    content_type="Videos",  # Direct enum value
    date="2026-06-08",
    url="https://youtube.com/...",
    views=200
)
```

## API Reference

Source: Advocu API Documentation
Endpoint: `POST /activity-drafts/content-creation`
Field: `contentType` (optional string enum)

Last Updated: 2026-06-08
