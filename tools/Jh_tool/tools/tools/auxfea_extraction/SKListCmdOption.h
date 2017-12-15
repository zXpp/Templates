#ifndef SK_LIST_CMD_OPTION_INC
#define SK_LIST_CMD_OPTION_INC

#include "CmdOption.h"

namespace Torch {

/** This class take a list of arguements

    @author John Dines (dines@idiap.ch)
    @see CmdLine
*/
class SKListCmdOption : public CmdOption
{
  public:
    /// Contains the file names after reading the command line.
    char **args;

    /// Number of items that have been read.
    int nargs;

    ///
    SKListCmdOption(const char *name_, const char *help_="", bool save_=false);

    virtual void read(int *argc_, char ***argv_);
    virtual void loadXFile(XFile *file);
    virtual void saveXFile(XFile *file);

    ~SKListCmdOption();
};

}

#endif
