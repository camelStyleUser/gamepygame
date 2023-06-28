#include <stdio.h>

#include <stdlib.h>

int main()

{

  char x;

  printf("Установщик gamepygame для arch-based linux\nпродолжить? [Y/N]");

  scanf("%c", &x);

  if(x == 'Y'){

    system("cd $HOME && sudo pacman -S python3 python-pip wget && pip install pygame && mkdir .gamepygame && echo \"python $HOME/.gamepygame/main.py\" >> && chmod +x $PREFIX/bin/gamepygame")
    printf("Введите gamepygame чтобы запустить игру.")

  }

}
