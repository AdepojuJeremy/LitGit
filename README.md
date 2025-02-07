# LitGit

LitGit is a lightweight Git implementation in Python that provides insights into version control system internals. This project implements core Git functionality while maintaining a clean, readable codebase that demonstrates version control concepts.

## Overview

LitGit provides a complete implementation of fundamental version control operations, offering both high-level commands for daily use and low-level access to internal operations. The project focuses on performance, reliability, and maintainability while adhering to Git's core design principles.

## Features

### Core Functionality

- Repository initialization and management
- File tracking and staging
- Commit creation and management
- Status monitoring and history viewing
- Object inspection and manipulation
- Tree visualization and traversal
- Reference and tag management
- Revision parsing and control
- Gitignore pattern handling

### Command Reference

```bash
litgit init          # Initialize repository
litgit add          # Stage files
litgit commit       # Create commit
litgit status       # Show working tree status
litgit log          # Display commit history
litgit cat-file     # Provide content of repository objects
litgit hash-object  # Compute object ID
litgit ls-tree      # List tree contents
litgit checkout     # Switch branches or restore files
litgit show-ref     # List references
litgit tag          # Create, list, or verify tags
litgit rev-parse    # Parse revisions
litgit ls-files     # Show staged files
litgit check-ignore # Check pathnames against ignore rules
litgit rm           # Remove files
```

## Installation

### Prerequisites

- Python 3.10+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/litgit.git
cd litgit
```

2. Install in development mode:
```bash
pip install -e .
```

3. Verify installation:
```bash
litgit --help
```

## Technical Documentation

### Internal Architecture

#### Object Model

The system implements four fundamental object types:
- Blobs: File content storage
- Trees: Directory structure representation
- Commits: History and snapshot management
- Tags: Reference marking

#### Storage System

- Content-addressable storage using SHA-1/SHA-256
- Loose and packed object formats
- Delta compression for storage optimization
- Garbage collection for maintenance

#### Reference Management

- Branch implementation and handling
- Reference logging and tracking
- Tag support (lightweight and annotated)
- Reference directory organization

#### Index Operations

- Staging area management
- Path and mode handling
- Index file format implementation
- Stage inspection capabilities

#### Core Algorithms

- Three-way merge implementation
- Myers diff algorithm integration
- Conflict resolution system
- Path filtering and matching

#### Network Layer

- Protocol support (HTTPS, SSH, Git)
- Push/pull operation handling
- Pack transfer optimization
- Smart protocol implementation

## Development Roadmap

### Version 1.0

- [ ] Complete branching and merging system
- [ ] Remote repository support
- [ ] Advanced operation implementation
- [ ] Storage optimization
- [ ] Performance improvements
- [ ] Enhanced user interface

### Version 2.0

- [ ] Extended network capabilities
- [ ] Advanced security features
- [ ] Performance optimization tools
- [ ] Extended API support
- [ ] Plugin system implementation

## System Requirements

### Supported Platforms

- Linux (Ubuntu, Fedora, etc.)
- macOS
- Windows (via WSL or native Python)

### Dependencies

- Python 3.10+
- Standard library dependencies
- Optional: development tools listed in requirements-dev.txt

## Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Submit pull request

### Guidelines

- Follow PEP 8 style guidelines
- Maintain comprehensive documentation
- Include test coverage
- Update API documentation

## Project Structure

```
litgit/
├── src/
│   ├── commands/    # Command implementations
│   ├── core/        # Core functionality
│   └── utils/       # Utility functions
├── tests/           # Test suite
├── docs/            # Documentation
└── examples/        # Usage examples
```

## Testing

```bash
# Run test suite
python -m pytest

# Run with coverage
python -m pytest --cov=litgit
```

## Troubleshooting

### Common Issues

- Module import errors: Verify installation with `pip list | grep litgit`
- Command not found: Check PATH configuration
- Permission issues: Verify file permissions

### Platform-Specific

#### Windows
- Use WSL for optimal experience
- Verify Python PATH configuration
- Check line ending settings

## API Documentation

Comprehensive API documentation is available in the `/docs` directory:
- API Reference
- Implementation Details
- Integration Guide
- Development Setup

## License

MIT License. See [LICENSE](LICENSE) file for details.

## Support

- Issues: GitHub issue tracker
- Email: support@litgit-example.com

## Acknowledgments

- Git project for architectural inspiration
- Python community for development tools
- Project contributors

---

*LitGit: A Lightweight Git Implementation*
