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
CMAKE_SOURCE_DIR = /home/john/src/openavionics/gr-openavionics.backup

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/john/src/openavionics/gr-openavionics.backup/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-openavionics.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-openavionics.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-openavionics.dir/flags.make

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o: lib/CMakeFiles/gnuradio-openavionics.dir/flags.make
lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o: ../lib/square_ff_impl.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/john/src/openavionics/gr-openavionics.backup/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o"
	cd /home/john/src/openavionics/gr-openavionics.backup/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o -c /home/john/src/openavionics/gr-openavionics.backup/lib/square_ff_impl.cc

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.i"
	cd /home/john/src/openavionics/gr-openavionics.backup/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/john/src/openavionics/gr-openavionics.backup/lib/square_ff_impl.cc > CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.i

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.s"
	cd /home/john/src/openavionics/gr-openavionics.backup/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/john/src/openavionics/gr-openavionics.backup/lib/square_ff_impl.cc -o CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.s

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.requires:
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.requires

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.provides: lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/gnuradio-openavionics.dir/build.make lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.provides.build
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.provides

lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.provides.build: lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o

# Object files for target gnuradio-openavionics
gnuradio__openavionics_OBJECTS = \
"CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o"

# External object files for target gnuradio-openavionics
gnuradio__openavionics_EXTERNAL_OBJECTS =

lib/libgnuradio-openavionics.so: lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o
lib/libgnuradio-openavionics.so: /usr/lib/libboost_filesystem-mt.so
lib/libgnuradio-openavionics.so: /usr/lib/libboost_system-mt.so
lib/libgnuradio-openavionics.so: /usr/local/lib/libgruel.so
lib/libgnuradio-openavionics.so: /usr/local/lib/libgnuradio-core.so
lib/libgnuradio-openavionics.so: lib/CMakeFiles/gnuradio-openavionics.dir/build.make
lib/libgnuradio-openavionics.so: lib/CMakeFiles/gnuradio-openavionics.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX shared library libgnuradio-openavionics.so"
	cd /home/john/src/openavionics/gr-openavionics.backup/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-openavionics.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-openavionics.dir/build: lib/libgnuradio-openavionics.so
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/build

lib/CMakeFiles/gnuradio-openavionics.dir/requires: lib/CMakeFiles/gnuradio-openavionics.dir/square_ff_impl.cc.o.requires
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/requires

lib/CMakeFiles/gnuradio-openavionics.dir/clean:
	cd /home/john/src/openavionics/gr-openavionics.backup/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-openavionics.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/clean

lib/CMakeFiles/gnuradio-openavionics.dir/depend:
	cd /home/john/src/openavionics/gr-openavionics.backup/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/john/src/openavionics/gr-openavionics.backup /home/john/src/openavionics/gr-openavionics.backup/lib /home/john/src/openavionics/gr-openavionics.backup/build /home/john/src/openavionics/gr-openavionics.backup/build/lib /home/john/src/openavionics/gr-openavionics.backup/build/lib/CMakeFiles/gnuradio-openavionics.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/gnuradio-openavionics.dir/depend
