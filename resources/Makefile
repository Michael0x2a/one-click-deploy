# Wind River Workbench generated Makefile.
# Do not edit!!!
#
# The file ".wrmakefile" is the template used by the Wind River Workbench to
# generate the makefiles of this project. Add user-specific build targets and
# make rules only(!) in this project's ".wrmakefile" file. These will then be
# automatically dumped into the makefiles.

WIND_HOME := $(subst \,/,$(WIND_HOME))
WIND_BASE := $(subst \,/,$(WIND_BASE))
WIND_USR := $(subst \,/,$(WIND_USR))

all : pre_build main_all post_build

_clean ::
	@echo "make: removing targets and objects of `pwd`"

TRACE=0
TRACEON=$(TRACE:0=@)
TRACE_FLAG=$(TRACEON:1=)

MAKEFILE := Makefile

FLEXIBLE_BUILD := 1

BUILD_SPEC = PPC603gnu
DEBUG_MODE = 1
ifeq ($(DEBUG_MODE),1)
MODE_DIR := Debug
else
MODE_DIR := NonDebug
endif
OBJ_DIR := .
WS_ROOT_DIR := C:/WindRiver/wrwb-debugmode-workspace
PRJ_ROOT_DIR := $(WS_ROOT_DIR)/2012_MainRobot



#Global Build Macros
PROJECT_TYPE = DKM
DEFINES = 
EXPAND_DBG = 0


#BuildSpec specific Build Macros
VX_CPU_FAMILY = ppc
CPU = PPC603
TOOL_FAMILY = gnu
TOOL = gnu
TOOL_PATH = 
CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp -mlongcall
LIBPATH = 
LIBS = 

IDE_INCLUDES = -I$(WIND_BASE)/target/h/WPILib -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h 

IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 

IDE_DEFINES = 



#BuildTool flags
ifeq ($(DEBUG_MODE),1)
DEBUGFLAGS_C-Compiler = -g
DEBUGFLAGS_C++-Compiler = -g
DEBUGFLAGS_Linker = -g
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -g
else
DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
DEBUGFLAGS_Partial-Image-Linker = 
DEBUGFLAGS_Librarian = 
DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif


#Project Targets
PROJECT_TARGETS = SimpleTemplate/$(MODE_DIR)/SimpleTemplate.out \
	 SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage.o


#Rules

# SimpleTemplate
ifeq ($(DEBUG_MODE),1)
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
SimpleTemplate/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
SimpleTemplate/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h/WPILib -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h 
SimpleTemplate/$(MODE_DIR)/% : IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 
SimpleTemplate/$(MODE_DIR)/% : IDE_DEFINES = 
SimpleTemplate/$(MODE_DIR)/% : PROJECT_TYPE = DKM
SimpleTemplate/$(MODE_DIR)/% : DEFINES = 
SimpleTemplate/$(MODE_DIR)/% : EXPAND_DBG = 0
SimpleTemplate/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
SimpleTemplate/$(MODE_DIR)/% : CPU = PPC603
SimpleTemplate/$(MODE_DIR)/% : TOOL_FAMILY = gnu
SimpleTemplate/$(MODE_DIR)/% : TOOL = gnu
SimpleTemplate/$(MODE_DIR)/% : TOOL_PATH = 
SimpleTemplate/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp -mlongcall
SimpleTemplate/$(MODE_DIR)/% : LIBPATH = 
SimpleTemplate/$(MODE_DIR)/% : LIBS = 
SimpleTemplate/$(MODE_DIR)/% : OBJ_DIR := SimpleTemplate/$(MODE_DIR)

OBJECTS_SimpleTemplate = SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage.o

SimpleTemplate/$(MODE_DIR)/SimpleTemplate.out : $(OBJECTS_SimpleTemplate)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@";rm -f "$@";nmppc $(OBJECTS_SimpleTemplate) $(IDE_LIBRARIES) | tclsh $(WIND_BASE)/host/resource/hutils/tcl/munch.tcl -c ppc > $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc $(DEBUGFLAGS_Linker) $(CC_ARCH_SPEC) -fdollars-in-identifiers -Wall $(ADDED_CFLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES)  -o $(OBJ_DIR)/ctdt.o -c $(OBJ_DIR)/ctdt.c; $(TOOL_PATH)ccppc -r -nostdlib -Wl,-X -T $(WIND_BASE)/target/h/tool/gnu/ldscripts/link.OUT -o "$@" $(OBJ_DIR)/ctdt.o $(OBJECTS_SimpleTemplate) $(IDE_LIBRARIES) $(LIBPATH) $(LIBS)  $(ADDED_LIBPATH) $(ADDED_LIBS) && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

SimpleTemplate/$(MODE_DIR)/SimpleTemplate_compile_file : $(FILE) ;

_clean :: SimpleTemplate/$(MODE_DIR)/SimpleTemplate_clean

SimpleTemplate/$(MODE_DIR)/SimpleTemplate_clean : 
	$(TRACE_FLAG)if [ -d "SimpleTemplate" ]; then cd "SimpleTemplate"; rm -rf $(MODE_DIR); fi


# SimpleTemplate_partialImage
ifeq ($(DEBUG_MODE),1)
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -g
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -g
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -g
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -g
else
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C-Compiler = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_C++-Compiler = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Linker = -O2 -fstrength-reduce -fno-builtin
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Partial-Image-Linker = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Librarian = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEBUGFLAGS_Assembler = -O2 -fstrength-reduce -fno-builtin
endif
SimpleTemplate_partialImage/$(MODE_DIR)/% : IDE_INCLUDES = -I$(WIND_BASE)/target/h/WPILib -I$(WIND_BASE)/target/h/wrn/coreip -I$(WIND_BASE)/target/h 
SimpleTemplate_partialImage/$(MODE_DIR)/% : IDE_LIBRARIES = $(WIND_BASE)/target/lib/WPILib.a 
SimpleTemplate_partialImage/$(MODE_DIR)/% : IDE_DEFINES = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : PROJECT_TYPE = DKM
SimpleTemplate_partialImage/$(MODE_DIR)/% : DEFINES = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : EXPAND_DBG = 0
SimpleTemplate_partialImage/$(MODE_DIR)/% : VX_CPU_FAMILY = ppc
SimpleTemplate_partialImage/$(MODE_DIR)/% : CPU = PPC603
SimpleTemplate_partialImage/$(MODE_DIR)/% : TOOL_FAMILY = gnu
SimpleTemplate_partialImage/$(MODE_DIR)/% : TOOL = gnu
SimpleTemplate_partialImage/$(MODE_DIR)/% : TOOL_PATH = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : CC_ARCH_SPEC = -mcpu=603 -mstrict-align -mno-implicit-fp -mlongcall
SimpleTemplate_partialImage/$(MODE_DIR)/% : LIBPATH = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : LIBS = 
SimpleTemplate_partialImage/$(MODE_DIR)/% : OBJ_DIR := SimpleTemplate_partialImage/$(MODE_DIR)

SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Client/xbox.o : $(PRJ_ROOT_DIR)/Code/Client/xbox.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Definitions/components.o : $(PRJ_ROOT_DIR)/Code/Definitions/components.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/MainRobot.o : $(PRJ_ROOT_DIR)/Code/Profiles/MainRobot.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/PrototypeRobot.o : $(PRJ_ROOT_DIR)/Code/Profiles/PrototypeRobot.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/SidewaysRobot.o : $(PRJ_ROOT_DIR)/Code/Profiles/SidewaysRobot.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/arm.o : $(PRJ_ROOT_DIR)/Code/Subsystems/arm.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/driving.o : $(PRJ_ROOT_DIR)/Code/Subsystems/driving.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/elevator.o : $(PRJ_ROOT_DIR)/Code/Subsystems/elevator.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/filter.o : $(PRJ_ROOT_DIR)/Code/Subsystems/filter.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/pid_drive.o : $(PRJ_ROOT_DIR)/Code/Subsystems/pid_drive.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/shooter.o : $(PRJ_ROOT_DIR)/Code/Subsystems/shooter.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/target.o : $(PRJ_ROOT_DIR)/Code/Tracking/target.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/track_silver.o : $(PRJ_ROOT_DIR)/Code/Tracking/track_silver.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/communication.o : $(PRJ_ROOT_DIR)/Code/communication.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/main_entry_point.o : $(PRJ_ROOT_DIR)/Code/main_entry_point.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/sensors.o : $(PRJ_ROOT_DIR)/Code/sensors.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/testing.o : $(PRJ_ROOT_DIR)/Code/testing.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/tools.o : $(PRJ_ROOT_DIR)/Code/tools.cpp $(FORCE_FILE_BUILD)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc $(DEBUGFLAGS_C++-Compiler) $(CC_ARCH_SPEC) -ansi -Wall  -MD -MP -mlongcall $(ADDED_C++FLAGS) $(IDE_INCLUDES) $(ADDED_INCLUDES) -DCPU=$(CPU) -DTOOL_FAMILY=$(TOOL_FAMILY) -DTOOL=$(TOOL) -D_WRS_KERNEL   $(DEFINES) -o "$@" -c "$<"


OBJECTS_SimpleTemplate_partialImage = SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Client/xbox.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Definitions/components.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/MainRobot.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/PrototypeRobot.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/SidewaysRobot.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/arm.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/driving.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/elevator.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/filter.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/pid_drive.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/shooter.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/target.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/track_silver.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/communication.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/main_entry_point.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/sensors.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/testing.o \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/tools.o

SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage.o : $(OBJECTS_SimpleTemplate_partialImage)
	$(TRACE_FLAG)if [ ! -d "`dirname "$@"`" ]; then mkdir -p "`dirname "$@"`"; fi;echo "building $@"; $(TOOL_PATH)ccppc -r -nostdlib -Wl,-X  -o "$@" $(OBJECTS_SimpleTemplate_partialImage) $(LIBPATH) $(LIBS) $(ADDED_LIBPATH) $(ADDED_LIBS)  && if [ "$(EXPAND_DBG)" = "1" ]; then plink "$@";fi

SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage_compile_file : $(FILE) ;

_clean :: SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage_clean

SimpleTemplate_partialImage/$(MODE_DIR)/SimpleTemplate_partialImage_clean : 
	$(TRACE_FLAG)if [ -d "SimpleTemplate_partialImage" ]; then cd "SimpleTemplate_partialImage"; rm -rf $(MODE_DIR); fi

force : 

DEP_FILES := SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Client/xbox.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Definitions/components.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/MainRobot.d \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/PrototypeRobot.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Profiles/SidewaysRobot.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/arm.d \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/driving.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/elevator.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/filter.d \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/pid_drive.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Subsystems/shooter.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/target.d \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/Tracking/track_silver.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/communication.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/main_entry_point.d \
	 SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/sensors.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/testing.d SimpleTemplate_partialImage/$(MODE_DIR)/Objects/2012_MainRobot/Code/tools.d
-include $(DEP_FILES)



-include $(PRJ_ROOT_DIR)/*.makefile

-include *.makefile

main_all : external_build $(PROJECT_TARGETS)
	@echo "make: built targets of `pwd`"

# entry point for extending the build
external_build ::
	@echo ""

# main entry point for pre processing prior to the build
pre_build :: $(PRE_BUILD_STEP) generate_sources
	@echo ""

# entry point for generating sources prior to the build
generate_sources ::
	@echo ""

# main entry point for post processing after the build
post_build :: $(POST_BUILD_STEP) deploy_output
	@echo ""

# entry point for deploying output after the build
deploy_output ::
	@echo ""

clean :: external_clean $(CLEAN_STEP) _clean

# entry point for extending the build clean
external_clean ::
	@echo ""
