"""
Authentication & Permissions Setup
---------------------------------
- Token authentication is enabled via Django REST Framework settings.
- All API endpoints require authentication by default (see settings.py).
- Token retrieval endpoint is available at /api-token-auth/ using DRF's obtain_auth_token view.
- Permission classes can be customized per viewset (see BookViewSet).
- Example usage: Send POST to /api-token-auth/ with username & password to get token.
- Include token in Authorization header as 'Token <your_token>' for authenticated requests.
"""
