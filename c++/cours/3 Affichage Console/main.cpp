#include <iostream>

/*
    std::cout : affichage standard (dans un buffer)
    std::cerr : erreurs (pas de buffer)
    std::clog : journalisation (dans un buffer)

    std::endl : \n + flush
*/

int main()
{
    std::cout << "Hello World!" << std::endl;
    std::cerr << "Hello World!" << std::endl;
    std::clog << "Hello World!" << std::endl;
    return 0;
}