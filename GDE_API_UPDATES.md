# GDE API Updates - 2026-06-08

## Summary

Completely rewritten GDE activity models and server functions to match the exact API specification from the official Advocu API documentation.

## Key Changes

### 1. Models (`src/models/gde.py`)

All GDE models were rewritten to match the API spec:

#### Content Creation
- Uses `contentType` (not `content_type`)
- Uses `activityDate` (not `date`)
- Uses `activityUrl` (not `url`)
- Metrics uses `readers` (not `views`)
- All fields are now optional
- Uses camelCase for all fields

#### Public Speaking
- Uses `activityDate`, `activityUrl`, `additionalInfo`
- Uses `eventFormat`, `country`, `inPersonAttendees`
- Removed fields: `event_name`, `location` (mapped to description and country)

#### Workshop
- Same structure as Public Speaking
- Uses `inPersonAttendees` instead of `attendees`

#### Mentoring
- Same structure as Public Speaking and Workshop
- Uses `inPersonAttendees` instead of `mentees`

#### Product Feedback
- Uses `contentType` (enum with 2 values)
- Uses `productDescription` (not `product_name`)
- Removed `feedback_type` and `impact` as separate top-level fields
- Maps `feedback_type` to `contentType`

#### Interaction with Googlers
- Uses `interactionType` (camelCase)
- Uses `format` field
- Uses `additionalLinks` (not `url`)
- Stores `googler_team` in `additionalInfo`

#### Stories
- Uses `whyIsSignificant` field
- Uses `significanceType` (not `story_type`)
- Uses `activityUrl`

### 2. Server Functions (`src/server.py`)

All `submit_gde_*` functions were updated to:

1. Use new model imports from `.models.gde`
2. Map user-friendly parameters to API field names
3. Build proper payloads with camelCase fields
4. Use `model_dump(exclude_none=True)` instead of `model_dump(mode='json', exclude_none=True)`
5. Remove the `by_alias` complexity since fields are named correctly now

### 3. Field Mappings

Common mappings across all GDE functions:

| User Parameter | API Field |
|----------------|-----------|
| `date` | `activityDate` |
| `url` | `activityUrl` |
| `views` | `metrics.readers` |
| `event_name` | Included in `description` |
| `location` | `country` |
| `attendees` | `inPersonAttendees` |
| `mentees` | `inPersonAttendees` |
| `topics` | Included in `description` |
| `product_name` | `productDescription` |
| `feedback_type` | `contentType` |
| `googler_team` | `additionalInfo` |
| `interaction_type` | `interactionType` |
| `story_type` | `significanceType` |
| `impact` | `whyIsSignificant` |

## Files Changed

- ✅ `src/models/gde.py` - Completely rewritten
- ✅ `src/server.py` - All 7 `submit_gde_*` functions updated
- ⚠️ `src/models/base.py` - No longer used by GDE (safe to delete, but kept for now)

## Docker Captain Models

**IMPORTANT:** No Docker Captain models or functions were modified. All Docker Captain functionality remains unchanged and working.

## Testing

To test the new GDE functions, restart the MCP server:

```bash
pkill -f "fastmcp run"
# Then reconnect with /mcp command
```

## Example Payload

### Content Creation (Before)
```json
{
  "title": "My Video",
  "date": "2026-06-08T00:00:00",
  "url": "https://example.com",
  "content_type": "video",
  "views": 200
}
```

### Content Creation (After)
```json
{
  "title": "My Video",
  "activityDate": "2026-06-08",
  "activityUrl": "https://example.com",
  "contentType": "video",
  "metrics": {
    "readers": 200
  }
}
```

## Next Steps

1. Test content creation submission
2. If needed, identify valid enum values for `contentType` from API errors
3. Add enum validation to models once valid values are known
4. Consider adding more parameters (tags, additionalInfo) to tool signatures
