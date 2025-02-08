Name:           aider
Version:        0.74.0
Release:        %autorelease
Summary:        Command-line AI coding assistant

License:        MIT
URL:            https://github.com/paul-gauthier/aider

BuildArch:      noarch

BuildRequires:  python3.12
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

# Runtime dependency for Python
Requires:       python3.12

%description
Aider is a terminal-based coding assistant that lets you program with 
LLM models like GPT-4 or Claude. It helps maintain conversation context
and can directly edit code files based on the AI's suggestions.

%prep
# Nothing to prep

%build
# Nothing to build

%install
# Create the directory for aider under the Python library directory.
mkdir -p %{buildroot}%{_libdir}/aider

# Create a Python virtual environment for aider.
python3.12 -m venv %{buildroot}%{_libdir}/aider/venv

# Install aider-chat into the virtual environment (without its dependencies).
%{buildroot}%{_libdir}/aider/venv/bin/pip install --no-deps aider-chat==%{version}

# Remove buildroot references from the venv’s text files.
# First, fix all the scripts in the venv's bin directory.
find %{buildroot}%{_libdir}/aider/venv/bin -type f -exec sed -i "s|%{buildroot}||g" {} +
# Then fix the venv configuration file.
sed -i "s|%{buildroot}||g" %{buildroot}%{_libdir}/aider/venv/pyvenv.cfg

# Create the binary directory and symlink the aider executable.
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/aider/venv/bin/aider %{buildroot}%{_bindir}/aider

%files
%dir %{_libdir}/aider
%{_libdir}/aider/venv
%attr(755,root,root) %{_bindir}/aider

%changelog
%autochangelog
