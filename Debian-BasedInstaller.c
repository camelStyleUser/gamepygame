#include <stdio.h>

#include <stdlib.h>

int main()

{

  char x;

  printf("Установщик gamepygame для debian-based linux\nпродолжить? [Y/N]");

  scanf("%c", &x);

  if(x == 'Y'){

    system("cd $HOME && sudo apt install python3 wget && pip install pygame && mkdir DGUN && echo \"python $HOME/gamepygame/main.py\" >> && chmod +x $PREFIX/bin/gamepygame")
    printf("Введите gamepygame чтобы запустить игру.")

  }

}
