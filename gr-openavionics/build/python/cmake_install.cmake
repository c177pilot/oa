# Install script for directory: /home/john/src/openavionics/gr-openavionics.backup/python

# Set the install prefix
IF(NOT DEFINED CMAKE_INSTALL_PREFIX)
  SET(CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT DEFINED CMAKE_INSTALL_PREFIX)
STRING(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
IF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  IF(BUILD_TYPE)
    STRING(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  ELSE(BUILD_TYPE)
    SET(CMAKE_INSTALL_CONFIG_NAME "Release")
  ENDIF(BUILD_TYPE)
  MESSAGE(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
ENDIF(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)

# Set the component getting installed.
IF(NOT CMAKE_INSTALL_COMPONENT)
  IF(COMPONENT)
    MESSAGE(STATUS "Install component: \"${COMPONENT}\"")
    SET(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  ELSE(COMPONENT)
    SET(CMAKE_INSTALL_COMPONENT)
  ENDIF(COMPONENT)
ENDIF(NOT CMAKE_INSTALL_COMPONENT)

# Install shared libraries without execute permission?
IF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  SET(CMAKE_INSTALL_SO_NO_EXE "1")
ENDIF(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/openavionics" TYPE FILE FILES
    "/home/john/src/openavionics/gr-openavionics.backup/python/__init__.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/square3_ff.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/serial_io.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/ahrs_parser.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/eis_parser.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/gns430_parser.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/ahrs_to_fg.py"
    "/home/john/src/openavionics/gr-openavionics.backup/python/gns430_to_fg.py"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

IF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  FILE(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/openavionics" TYPE FILE FILES
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/__init__.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/square3_ff.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/serial_io.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/ahrs_parser.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/eis_parser.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/gns430_parser.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/ahrs_to_fg.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/gns430_to_fg.pyc"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/__init__.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/square3_ff.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/serial_io.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/ahrs_parser.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/eis_parser.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/gns430_parser.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/ahrs_to_fg.pyo"
    "/home/john/src/openavionics/gr-openavionics.backup/build/python/gns430_to_fg.pyo"
    )
ENDIF(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")

