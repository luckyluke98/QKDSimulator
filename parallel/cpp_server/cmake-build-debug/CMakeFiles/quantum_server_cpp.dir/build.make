# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/quantum_server_cpp.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/quantum_server_cpp.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/quantum_server_cpp.dir/flags.make

CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o: CMakeFiles/quantum_server_cpp.dir/flags.make
CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o: ../src/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o -c /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/main.cpp

CMakeFiles/quantum_server_cpp.dir/src/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quantum_server_cpp.dir/src/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/main.cpp > CMakeFiles/quantum_server_cpp.dir/src/main.cpp.i

CMakeFiles/quantum_server_cpp.dir/src/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quantum_server_cpp.dir/src/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/main.cpp -o CMakeFiles/quantum_server_cpp.dir/src/main.cpp.s

CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o: CMakeFiles/quantum_server_cpp.dir/flags.make
CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o: ../src/circuit.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o -c /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/circuit.cpp

CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/circuit.cpp > CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.i

CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/circuit.cpp -o CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.s

CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o: CMakeFiles/quantum_server_cpp.dir/flags.make
CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o: ../src/multi_thread_server.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o -c /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/multi_thread_server.cpp

CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/multi_thread_server.cpp > CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.i

CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/multi_thread_server.cpp -o CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.s

CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o: CMakeFiles/quantum_server_cpp.dir/flags.make
CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o: ../src/quantum_manager.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o -c /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/quantum_manager.cpp

CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/quantum_manager.cpp > CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.i

CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/quantum_manager.cpp -o CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.s

CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o: CMakeFiles/quantum_server_cpp.dir/flags.make
CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o: ../src/utils.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o -c /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/utils.cpp

CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/utils.cpp > CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.i

CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/src/utils.cpp -o CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.s

# Object files for target quantum_server_cpp
quantum_server_cpp_OBJECTS = \
"CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o" \
"CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o" \
"CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o" \
"CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o" \
"CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o"

# External object files for target quantum_server_cpp
quantum_server_cpp_EXTERNAL_OBJECTS =

quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/src/main.cpp.o
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/src/circuit.cpp.o
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/src/multi_thread_server.cpp.o
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/src/quantum_manager.cpp.o
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/src/utils.cpp.o
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/build.make
quantum_server_cpp: CMakeFiles/quantum_server_cpp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX executable quantum_server_cpp"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/quantum_server_cpp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/quantum_server_cpp.dir/build: quantum_server_cpp

.PHONY : CMakeFiles/quantum_server_cpp.dir/build

CMakeFiles/quantum_server_cpp.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/quantum_server_cpp.dir/cmake_clean.cmake
.PHONY : CMakeFiles/quantum_server_cpp.dir/clean

CMakeFiles/quantum_server_cpp.dir/depend:
	cd /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug /Users/alexkolar/Desktop/Argonne/CLion/quantum_server_cpp/cmake-build-debug/CMakeFiles/quantum_server_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/quantum_server_cpp.dir/depend

