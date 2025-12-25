#!/bin/bash
# Quick start script for Jekyll development

# Set Ruby path to use Homebrew version
export PATH="/usr/local/opt/ruby/bin:$PATH"
export SDKROOT="/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk"
export CPLUS_INCLUDE_PATH="$SDKROOT/usr/include/c++/v1"
export CXXFLAGS="-I$SDKROOT/usr/include/c++/v1"

echo "🚀 Starting Jekyll development server..."
echo ""
echo "Ruby version: $(ruby -v)"
echo "Bundler version: $(bundle -v)"
echo ""

# Start Jekyll with live reload
bundle exec jekyll serve --livereload
