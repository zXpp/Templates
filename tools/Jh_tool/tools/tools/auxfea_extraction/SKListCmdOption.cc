#include "SKListCmdOption.h"
#include "DiskXFile.h"

namespace Torch {

SKListCmdOption::SKListCmdOption(const char *name_, const char *help_, bool save_)
  : CmdOption(name_, "<arg list ...>", help_, save_)
{
  nargs = 0;
  args = NULL;
}

void SKListCmdOption::read(int *argc_, char ***argv_)
{
  nargs = *argc_;

  //fprintf(stderr,"nargs: %i\n",nargs);

  if(nargs == 0)
    error("SKListCmdOption: must be at least one arguement");

  /// Read the contents of the list...
  args = (char**)allocator->alloc(sizeof(char *)*nargs);
  for (int i = 0; i < nargs; i++){
    args[i] = **argv_;
    //fprintf(stderr,"%s ", args[i]);
    (*argv_)++;
  }
  // fprintf(stderr,"\n");

  //message("SKListCmdOption: %d arguements detected", nargs);

  ////////////////////////////////////

  (*argc_) = 0;
}

void SKListCmdOption::loadXFile(XFile *file)
{
  file->taggedRead(&nargs, sizeof(int), 1, "NARGS");
  args = (char **)allocator->alloc(sizeof(char *)*nargs);  
  for(int i = 0; i < nargs; i++)
  {
    int melanie;
    file->taggedRead(&melanie, sizeof(int), 1, "SIZE");
    args[i] = (char *)allocator->alloc(melanie);
    file->taggedRead(args[i], 1, melanie, "ARG");
  }
}

void SKListCmdOption::saveXFile(XFile *file)
{
  file->taggedWrite(&nargs, sizeof(int), 1, "NARGS");
  for(int i = 0; i < nargs; i++)
  {
    int melanie = strlen(args[i])+1;
    file->taggedWrite(&melanie, sizeof(int), 1, "SIZE");
    file->taggedWrite(args[i], 1, melanie, "ARG");
  }
}

SKListCmdOption::~SKListCmdOption()
{
}

}
