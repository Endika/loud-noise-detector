## Contributing

This project uses [Semantic Release](https://python-semantic-release.readthedocs.io/) for versioning.

### Commit message format

Your commit messages must follow this format to trigger automatic version updates:

- `feat(component): Add new feature` - Minor version bump (0.x.0)
- `fix(component): Fix a bug` - Patch version bump (0.0.x)
- `perf(component): Improve performance` - Patch version bump (0.0.x)
- `docs(component): Update documentation` - No version bump
- `style(component): Fix formatting` - No version bump
- `refactor(component): Refactor code` - No version bump
- `test(component): Add tests` - No version bump
- `chore(component): Update tooling` - No version bump

### Workflow

1. Make your changes
2. Commit with appropriate message format
3. Push to your branch
4. Create a pull request
5. When merged to main, a new version will be released automatically if needed

### Manual release

```bash
make version  # Update version number based on commits
make publish  # Create a release
```
