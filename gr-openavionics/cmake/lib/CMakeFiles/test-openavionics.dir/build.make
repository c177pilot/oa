# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/cmake-gui

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/john/src/openavionics/gr-openavionics

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/john/src/openavionics/gr-openavionics/cmake

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-openavionics.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-openavionics.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-openavionics.dir/flags.make

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o: lib/CMakeFiles/test-openavionics.dir/flags.make
lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o: ../lib/test_openavionics.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/john/src/openavionics/gr-openavionics/cmake/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test-openavionics.dir/test_openavionics.cc.o -c /home/john/src/openavionics/gr-openavionics/lib/test_openavionics.cc

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-openavionics.dir/test_openavionics.cc.i"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/john/src/openavionics/gr-openavionics/lib/test_openavionics.cc > CMakeFiles/test-openavionics.dir/test_openavionics.cc.i

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-openavionics.dir/test_openavionics.cc.s"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/john/src/openavionics/gr-openavionics/lib/test_openavionics.cc -o CMakeFiles/test-openavionics.dir/test_openavionics.cc.s

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.requires:
.PHONY : lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.requires

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.provides: lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-openavionics.dir/build.make lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.provides

lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.provides.build: lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o: lib/CMakeFiles/test-openavionics.dir/flags.make
lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o: ../lib/qa_openavionics.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/john/src/openavionics/gr-openavionics/cmake/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o -c /home/john/src/openavionics/gr-openavionics/lib/qa_openavionics.cc

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-openavionics.dir/qa_openavionics.cc.i"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/john/src/openavionics/gr-openavionics/lib/qa_openavionics.cc > CMakeFiles/test-openavionics.dir/qa_openavionics.cc.i

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-openavionics.dir/qa_openavionics.cc.s"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/john/src/openavionics/gr-openavionics/lib/qa_openavionics.cc -o CMakeFiles/test-openavionics.dir/qa_openavionics.cc.s

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.requires:
.PHONY : lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.requires

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.provides: lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-openavionics.dir/build.make lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.provides

lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.provides.build: lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o

# Object files for target test-openavionics
test__openavionics_OBJECTS = \
"CMakeFiles/test-openavionics.dir/test_openavionics.cc.o" \
"CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o"

# External object files for target test-openavionics
test__openavionics_EXTERNAL_OBJECTS =

lib/test-openavionics: lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o
lib/test-openavionics: lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o
lib/test-openavionics: /usr/local/lib/libgnuradio-core.so
lib/test-openavionics: /usr/lib/libboost_filesystem-mt.so
lib/test-openavionics: /usr/lib/libboost_system-mt.so
lib/test-openavionics: /usr/lib/libcppunit.so
lib/test-openavionics: lib/libgnuradio-openavionics.so
lib/test-openavionics: /usr/lib/libboost_filesystem-mt.so
lib/test-openavionics: /usr/lib/libboost_system-mt.so
lib/test-openavionics: /usr/local/lib/libgruel.so
lib/test-openavionics: /usr/local/lib/libgnuradio-core.so
lib/test-openavionics: lib/CMakeFiles/test-openavionics.dir/build.make
lib/test-openavionics: lib/CMakeFiles/test-openavionics.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable test-openavionics"
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-openavionics.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-openavionics.dir/build: lib/test-openavionics
.PHONY : lib/CMakeFiles/test-openavionics.dir/build

lib/CMakeFiles/test-openavionics.dir/requires: lib/CMakeFiles/test-openavionics.dir/test_openavionics.cc.o.requires
lib/CMakeFiles/test-openavionics.dir/requires: lib/CMakeFiles/test-openavionics.dir/qa_openavionics.cc.o.requires
.PHONY : lib/CMakeFiles/test-openavionics.dir/requires

lib/CMakeFiles/test-openavionics.dir/clean:
	cd /home/john/src/openavionics/gr-openavionics/cmake/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-openavionics.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-openavionics.dir/clean

lib/CMakeFiles/test-openavionics.dir/depend:
	cd /home/john/src/openavionics/gr-openavionics/cmake && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/john/src/openavionics/gr-openavionics /home/john/src/openavionics/gr-openavionics/lib /home/john/src/openavionics/gr-openavionics/cmake /home/john/src/openavionics/gr-openavionics/cmake/lib /home/john/src/openavionics/gr-openavionics/cmake/lib/CMakeFiles/test-openavionics.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-openavionics.dir/depend

