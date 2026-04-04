# StatSync
A visualizer for personal fitness data

Usage and installation instructions coming soon...


TODO (no particular order):
- [DONE] Auth
- Create home/dash/profile page
    - This will also entail coming up with stats to include/calculate. It may make sense for this to be broken up into tabs/sections, but a single dashboard will suffice as an MVP.
- Redirect to home after auth
    - Currently, the user is left on auth page, redirect to a dashboard or profile page or something
- Cache/store data
    - Possibly two method, CSV and SQLite. SQLite is lightweight enough to store locally and makes for nice filtering. CSV is convenient and easy to process. Both of these make data available offline and help prevent unecessary API requests. Caching could be useful but may not be necessary

Possible future directions
- Enable writing/editing
