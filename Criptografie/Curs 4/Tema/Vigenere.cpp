#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    int chei [] = {0, 12, 1, 2, 16};
    int counter = 0;
    for (int j = 'a' ; j <= 'z'; j++){
        cout << "beta " << counter ++ << ": ";
        for (int i = 0; i < 5; i++) {
            unsigned char caracter = (unsigned char) ((j + chei[i]));
            if (caracter > 'z')
                cout << (unsigned char)(caracter - 26) ;// << (int) caracter;
            else
                cout << caracter ;// << (int) caracter;
        }
        cout << endl;
        //cout << "#########################\n";
    }
    char key [] = "coder";
    char criptat[] = "togmggbymkkcqivdmlxkkbyifvcuekcuuisvvxqspwwejkoqggphumtwhlsfyovwwknhhmrcqfqvvhkwpsuedugrsfctwijkhvfathkeffwptjggvivcgdrapgwvmosqxghkdvtwhuevkcwyjpsgsngfwsljsfseooqhwtofshaciingfbifgabgjadwsytopmlecqzwasgvsfwrqsfsfvqrhdrsnmvmkcbhrvkblxkgzi";
    int lungimeCriptat = strlen(criptat); 
    cout << key << endl;
    cout << "mesaj decriptat: " << criptat;
    for (int i = 0, j = 0; i <lungimeCriptat; i++){
        unsigned char caracter = (unsigned char) ((criptat[i] - key[j++]));
        // if (caracter < 'a'){
        //     cout << (unsigned char)(caracter + 26) ;
        // } else {
            cout << caracter;
        //}
        if (j > 4)
            j = 0;
    }
    return 0;
}