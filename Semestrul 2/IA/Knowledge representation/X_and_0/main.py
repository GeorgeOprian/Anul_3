import time

import pygame, sys, os
import statistics as stats

ADANCIME_MAX = 6


def elem_identice(lista):
    if (all(elem == lista[0] for elem in lista[1:])):
        return lista[0] if lista[0] != Joc.GOL else False
    return False


class Joc:
    """
    Clasa care defineste jocul. Se va schimba de la un joc la altul.
    """
    NR_COLOANE = 10
    JMIN = None
    JMAX = None
    GOL = '#'
    NR_LINII = 10

    SCOR_X = 0
    SCOR_0 = 0
    CASTIGATOR = '#'

    @classmethod
    def initializeaza(cls, display, NR_COLOANE=10, dim_celula=50):
        cls.display = display
        cls.dim_celula = dim_celula
        cls.x_img = pygame.image.load('ics.png')
        cls.x_img = pygame.transform.scale(cls.x_img, (dim_celula, dim_celula))
        cls.zero_img = pygame.image.load('zero.png')
        cls.zero_img = pygame.transform.scale(cls.zero_img, (dim_celula, dim_celula))
        cls.celuleGrid = []  # este lista cu patratelele din grid
        for linie in range(NR_COLOANE):
            for coloana in range(NR_COLOANE):
                patr = pygame.Rect(coloana * (dim_celula + 1), linie * (dim_celula + 1), dim_celula, dim_celula)
                cls.celuleGrid.append(patr)

    def deseneaza_grid(self, marcaj=None):  # tabla de exemplu este ["#","x","#","0",......]
        if Joc.CASTIGATOR != '#':
            if Joc.CASTIGATOR == 'x':
                castigator = 'x'
            else:
                castigator = '0'
        for ind in range(len(self.matr)):
            linie = ind // Joc.NR_LINII
            coloana = ind % Joc.NR_COLOANE

            if marcaj == ind:
                # daca am o patratica selectata, o desenez cu rosu
                culoare = (255, 0, 0)
            else:
                # altfel o desenez cu alb
                culoare = (255, 255, 255)
            if self.l_jum1piesa != -1 and self.c_jum1piesa != -1 and ind == (Joc.NR_LINII * self.l_jum1piesa + self.c_jum1piesa):
                culoare = (111, 191, 132) #daca am plasat jumatate de piesa colorez jumatatea de piesa cu verde deschis

            if Joc.CASTIGATOR != '#' and self.matr[ind] == castigator:
                culoare = (0, 255, 0)

            # [vec_diag, indici_vec_diag] = self.obtine_vecini_pe_diagonala(linie, coloana) #feature sugestii de plasare
            # if linie == 4 and coloana == 6:
            #     x = 1
            # if (self.l_jum1piesa != -1 and self.c_jum1piesa != -1) and (self.matr[ind] == self.__class__.GOL) \
            #     and (ind in indici_vec_diag):
            #     #     (ind == (self.l_jum1piesa - 1) * Joc.NR_COLOANE + self.c_jum1piesa - 1
            #     # or ind == (self.l_jum1piesa - 1) * Joc.NR_COLOANE + self.c_jum1piesa + 1
            #     # or ind == (self.l_jum1piesa + 1) * Joc.NR_COLOANE + self.c_jum1piesa + 1
            #     # or ind == (self.l_jum1piesa + 1) * Joc.NR_COLOANE + self.c_jum1piesa - 1):
            #     culoare = (0, 255, 0) # coloreaza vecinii cu verde

            pygame.draw.rect(self.__class__.display, culoare, self.__class__.celuleGrid[ind])  # alb = (255,255,255)
            if self.matr[ind] == 'x':
                self.__class__.display.blit(self.__class__.x_img, (
                coloana * (self.__class__.dim_celula + 1), linie * (self.__class__.dim_celula + 1)))
            elif self.matr[ind] == '0':
                self.__class__.display.blit(self.__class__.zero_img, (
                coloana * (self.__class__.dim_celula + 1), linie * (self.__class__.dim_celula + 1)))
        pygame.display.flip()  # obligatoriu pentru a actualiza interfata (desenul)



    def __init__(self, tabla=None):
        # self.matr=tabla or [self.__class__.GOL]*9
        self.matr = tabla or [self.__class__.GOL] * (Joc.NR_COLOANE * Joc.NR_LINII)
        self.matr[(Joc.NR_LINII // 2 - 1) * Joc.NR_COLOANE + (Joc.NR_COLOANE // 2 - 1)] = 'x'
        self.matr[(Joc.NR_LINII // 2 - 1) * Joc.NR_COLOANE + (Joc.NR_COLOANE // 2)] = '0'
        self.matr[(Joc.NR_LINII // 2) * Joc.NR_COLOANE + (Joc.NR_COLOANE // 2 - 1)] = '0'
        self.matr[(Joc.NR_LINII // 2) * Joc.NR_COLOANE + (Joc.NR_COLOANE // 2)] = 'x'

        self.l_jum1piesa = -1
        self.c_jum1piesa = -1


    @classmethod
    def jucator_opus(cls, jucator):
        return cls.JMAX if jucator == cls.JMIN else cls.JMIN

    def final(self):
        if self.__class__.GOL not in self.matr or self.matr.count(self.__class__.GOL) == 1:
            print("finalul jocului")
            return True #finalul jocului

        for i in range(len(self.matr)):
            for j in range(len(self.matr)):
                linie_i = i // 10
                coloana_i = i % 10
                linie_j = j // 10
                coloana_j = j % 10
                if (self.matr[i] == self.__class__.GOL and self.matr[j] == self.__class__.GOL): #daca mai am spatii libere pe diagonale mai pot face o mutare
                    if self.mutare_valida(linie_i, coloana_i) and self.pot_completa_placuta(linie_i, coloana_i, linie_j, coloana_j):
                        return False #nu s-a terminat jocul
        return True #finalul jocului

    def mutari(self, jucator_opus):
        l_mutari = []
        for i in range(len(self.matr)):
            for j in range(len(self.matr)):
                if self.matr[i] == self.__class__.GOL and self.matr[j] == self.__class__.GOL: #ambele pozitii sunt goale
                    linie_i = i // 10
                    coloana_i = i % 10
                    linie_j = j // 10
                    coloana_j = j % 10
                    if (self.matr[i] == Joc.GOL and self.matr[j] == Joc.GOL) \
                            and self.mutare_valida(linie_i, coloana_i) \
                            and self.pot_completa_placuta(linie_i, coloana_i, linie_j, coloana_j):
                        matr_tabla_noua = list(self.matr) #fac o copie a matricei
                        matr_tabla_noua[i] = jucator_opus
                        matr_tabla_noua[j] = jucator_opus
                        l_mutari.append(Joc(matr_tabla_noua))

        return l_mutari

    def linii_deschise(self, simbol):
        linii_deschise = 0
        for i in range(Joc.NR_LINII):
            linie = self.matr[(i * 10):(i+1)*10]
            strlinie = ''.join(linie)
            if len(linie) >= 3 and Joc.jucator_opus(simbol) not in strlinie:
                linii_deschise += 1
        return linii_deschise

    def coloane_deschise(self, simbol):
        coloane_deschise = 0
        for i in range(Joc.NR_COLOANE):
            coloana = self.matr[i:100:Joc.NR_COLOANE]
            strcoloana = ''.join(coloana)
            if len(coloana) >= 3 and Joc.jucator_opus(simbol) not in strcoloana:
                coloane_deschise += 1
        return coloane_deschise

    def estimeaza_scor(self, adancime):
        final = self.final()
        self.calculeaza_scor()
        if final:
            if Joc.SCOR_X == Joc.SCOR_0:
                t_final = "remiza"
            elif Joc.SCOR_X > Joc.SCOR_0:
                t_final = 'x'
            else:
                t_final = '0'
            if t_final == self.__class__.JMAX:
                return (99 + adancime)
            elif t_final == self.__class__.JMIN:
                return (-99 - adancime)
            elif t_final == 'remiza':
                return 0
        elif self.__class__.JMAX == 'x':
            return Joc.SCOR_X - Joc.SCOR_0
        else:
            return Joc.SCOR_0 - Joc.SCOR_X

    def estimeaza_scor2(self, adancime):
        final = self.final()
        self.calculeaza_scor()
        if final:
            if Joc.SCOR_X == Joc.SCOR_0:
                t_final = "remiza"
            elif Joc.SCOR_X > Joc.SCOR_0:
                t_final = 'x'
            else:
                t_final = '0'
            if t_final == self.__class__.JMAX:
                return (99 + adancime)
            elif t_final == self.__class__.JMIN:
                return (-99 - adancime)
            elif t_final == 'remiza':
                return 0
        return ((self.linii_deschise(self.__class__.JMAX) - self.linii_deschise(self.__class__.JMIN)) +
        (self.coloane_deschise(self.__class__.JMAX) - self.coloane_deschise(self.__class__.JMIN)))



    def calculeaza_scor(self):
        Joc.SCOR_X = 0
        Joc.SCOR_0 = 0

        # print("calculatorul estimeaza scorul")
        for i in range(Joc.NR_LINII):
            for j in range(Joc.NR_COLOANE):

                if self.matr[i * Joc.NR_COLOANE + j] != self.__class__.GOL and \
                        (j <= (Joc.NR_COLOANE - 3) and self.matr[i * Joc.NR_COLOANE + j] == self.matr[i * Joc.NR_COLOANE + j + 1]
                         and self.matr[i * Joc.NR_COLOANE + j + 1] == self.matr[i * Joc.NR_COLOANE + j + 2]):
                    # print ("intra pe primul if in calculeaza scor i = {} j = {} si testeaza {} {} {}".format(i, j, self.matr[i * Joc.NR_COLOANE + j], self.matr[i * Joc.NR_COLOANE + j + 1], self.matr[i * Joc.NR_COLOANE + j + 2] ))
                    if self.matr[i * Joc.NR_COLOANE + j] == 'x':
                        Joc.SCOR_X += 1
                    if self.matr[i * Joc.NR_COLOANE + j] == '0':
                        Joc.SCOR_0 += 1
                elif self.matr[i * Joc.NR_COLOANE + j] != self.__class__.GOL and \
                        (i <= (Joc.NR_COLOANE - 3) and self.matr[i * Joc.NR_COLOANE + j] == self.matr[i * Joc.NR_COLOANE + j + Joc.NR_COLOANE]
                         and self.matr[i * Joc.NR_COLOANE + j + Joc.NR_COLOANE] == self.matr[i * Joc.NR_COLOANE + j + 2 * Joc.NR_COLOANE]):
                    # print("intra pe al doilea if in calculeaza scor i = {} j = {} si testeaaza {} {} {}".format(i, j, self.matr[i * Joc.NR_COLOANE + j], self.matr[i * Joc.NR_COLOANE + j + Joc.NR_COLOANE], self.matr[i * Joc.NR_COLOANE + j + 2 * Joc.NR_COLOANE]))
                    if self.matr[i * Joc.NR_COLOANE + j] == 'x':
                        Joc.SCOR_X += 1
                    if self.matr[i * Joc.NR_COLOANE + j] == '0':
                        Joc.SCOR_0 += 1
        # print("calculatorul a terminat de estimat")

    def afiseaza_scor(self):
        print("--------------------------------")
        print("Scor:")
        print("X: {}".format(Joc.SCOR_X))
        print("0: {}".format(Joc.SCOR_0))
        print("--------------------------------")

    def afisare(self):
        sir="  |"
        sir+=" ".join([str(i) for i in range(Joc.NR_COLOANE)])+"\n"
        sir += " " * 2
        sir+="-"*((Joc.NR_COLOANE+1)*2 - 2)+"\n"
        for i in range(Joc.NR_COLOANE):
            sir+= str(i)+" |"+" ".join([str(x) for x in self.matr[Joc.NR_COLOANE*i : Joc.NR_COLOANE*(i+1)]])+"\n"
        return sir

    def __str__(self):
        return self.afisare()

    def vecin_pe_linii (self, linie, coloana):
        if (self.matr[linie * Joc.NR_COLOANE + coloana - 1] == 'x' or self.matr[linie * Joc.NR_COLOANE + coloana - 1] == '0'  #vecin pe linie in stanga
            or self.matr[linie * Joc.NR_COLOANE + coloana + 1] == 'x' or self.matr[linie * Joc.NR_COLOANE + coloana + 1] == '0'): #vecin pe linie in dreapta )
            return True
        return False

    def vecin_pe_coloane(self, linie, coloana):
        if (self.matr[(linie - 1) * Joc.NR_COLOANE + coloana] == 'x' or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana] == '0'  #vecin pe coloana deasupra
            or self.matr[(linie + 1) * Joc.NR_COLOANE + coloana] == 'x' or self.matr[(linie + 1) * Joc.NR_COLOANE + coloana] == '0'):
            return True
        return False

    def vecin_pe_diagonale(self, linie, coloana):
        if (self.matr[(linie - 1) * Joc.NR_COLOANE + coloana - 1] == 'x' or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana - 1] == '0' # vecin stanga sus
            or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana + 1] == 'x' or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana + 1] == '0' # vecin dreapta sus
            or self.matr[(linie + 1) * Joc.NR_COLOANE + coloana + 1] == 'x' or self.matr[(linie + 1) * Joc.NR_COLOANE + coloana + 1] == '0' # vecin dreapta jos
            or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana + 1] == 'x' or self.matr[(linie - 1) * Joc.NR_COLOANE + coloana - 1] == '0'):  # vecin stanga jos
            return True
        return False

    def obtine_lista_vecini(self, linie, coloana):
        lista_vecini = []

        if (linie * 10 + coloana) % 10 != 0:  # daca nu am plasat pe prima coloana caut vecin in stanga
            iv_stanga = (linie * 10 + coloana - 1)
            lista_vecini.append(self.matr[iv_stanga])  # vecin stanga

        if (linie * 10 + coloana) % 10 != 0 and (
                linie * 10 + coloana) > 9:  # daca nu am plasat pe prima linie sau prima coloana caut vecin in stanga sus
            iv_stanga_sus = ((linie - 1) * 10 + coloana - 1)
            lista_vecini.append(self.matr[iv_stanga_sus])  # stanga sus

        if (linie * 10 + coloana) > 9:  # daca nu am plasat pe prima linie caut vecin deasupra
            iv_deasupra = ((linie - 1) * 10 + coloana)
            lista_vecini.append(self.matr[iv_deasupra])  # vecin deasupra

        if (linie * 10 + coloana) > 9 and (
                linie * 10 + coloana) % 10 != 9:  # daca nu am plasat pe prima linie sau ultima coloana caut vecin in in dreapta sus
            iv_dreapta_sus = ((linie - 1) * 10 + coloana + 1)
            lista_vecini.append(self.matr[iv_dreapta_sus])  # dreapta sus

        if (linie * 10 + coloana) % 10 != 9:  # daca nu am plasat  pe ultima coloana caut veci in dreapta
            iv_dreapta = linie * 10 + coloana + 1
            lista_vecini.append(self.matr[iv_dreapta])  # vecin dreapta

        if (linie * 10 + coloana) < 90 and (
                linie * 10 + coloana) % 10 != 9:  # daca nu am plasat pe ultima linie sau prima coloana caut vecin in dreapta jos
            iv_dreapta_jos = ((linie + 1) * 10 + coloana + 1)
            lista_vecini.append(self.matr[iv_dreapta_jos])  # dreapta jos

        if (linie * 10 + coloana) < 90:  # daca nu am plasat pe ultima linie caut vecin dedesubt
            iv_dedesubt = ((linie + 1) * 10 + coloana)
            lista_vecini.append(self.matr[iv_dedesubt])  # vecin dedesubt

        if (linie * 10 + coloana) % 10 != 0 and (
                linie * 10 + coloana) < 90:  # daca nu am plasat pe ultima linie si prima coloana caut vecin in stanga jos
            iv_stanga_jos = ((linie + 1) * 10 + coloana - 1)
            lista_vecini.append(self.matr[iv_stanga_jos])  # stanga jos

        return lista_vecini

    def obtine_vecini_pe_diagonala(self, linie, coloana):
        lista_vecini = []
        ind_vecini =[]
        if (linie * 10 + coloana) % 10 != 0 and (
                linie * 10 + coloana) > 9:  # daca nu am plasat pe prima linie sau prima coloana caut vecin in stanga sus
            iv_stanga_sus = ((linie - 1) * 10 + coloana - 1)
            lista_vecini.append(self.matr[iv_stanga_sus])  # stanga sus
            ind_vecini.append(iv_stanga_sus)

        if (linie * 10 + coloana) > 9 and (
                linie * 10 + coloana) % 10 != 9:  # daca nu am plasat pe prima linie sau ultima coloana caut vecin in in dreapta sus
            iv_dreapta_sus = ((linie - 1) * 10 + coloana + 1)
            lista_vecini.append(self.matr[iv_dreapta_sus])  # dreapta sus
            ind_vecini.append(iv_dreapta_sus)

        if (linie * 10 + coloana) < 90 and (
                linie * 10 + coloana) % 10 != 9:  # daca nu am plasat pe ultima linie sau prima coloana caut vecin in dreapta jos
            iv_dreapta_jos = ((linie + 1) * 10 + coloana + 1)
            lista_vecini.append(self.matr[iv_dreapta_jos])  # dreapta jos
            ind_vecini.append(iv_dreapta_jos)

        if (linie * 10 + coloana) % 10 != 0 and (
                linie * 10 + coloana) < 90:  # daca nu am plasat pe ultima linie si prima coloana caut vecin in stanga jos
            iv_stanga_jos = ((linie + 1) * 10 + coloana - 1)
            lista_vecini.append(self.matr[iv_stanga_jos])  # stanga jos
            ind_vecini.append(iv_stanga_jos)

        return lista_vecini, ind_vecini

    #o mutare valida inseamna sa am printe vecini atat un x cat si un 0
    def mutare_valida(self, linie, coloana):
        #primul x are ca vecin si un x si un 0
        # if self.vecin_pe_linii(linie, coloana) or self.vecin_pe_coloane(linie, coloana) or self.vecin_pe_diagonale(linie,coloana):  # vecin pe coloana dedesubt
        #     return True
        lista_vecini = self.obtine_lista_vecini(linie, coloana)
        [vecini_pe_diagonala, indici] = self.obtine_vecini_pe_diagonala(linie, coloana)
        # print ("linie {} coloana {} vecini pe diagonala: {}".format(linie, coloana, vecini_pe_diagonala))
        if 'x' in lista_vecini and '0' in lista_vecini and '#' in vecini_pe_diagonala:
            # if
            return True
        return False
    # verifica daca linia si coloana data ca parametri sunt pe diagonala cu pozitia pe care am plasat deja jumatate de placuta
    def pot_completa_placuta(self, linie_jum_piesa, coloana_jum_piesa, linie, coloana):
        if ((linie_jum_piesa == linie - 1 and coloana_jum_piesa == coloana - 1) # stanga sus
            or (linie_jum_piesa == linie - 1 and coloana_jum_piesa == coloana + 1) #dreapta sus
            or (linie_jum_piesa == linie + 1 and coloana_jum_piesa == coloana + 1)  # dreapta jos
            or (linie_jum_piesa == linie + 1 and coloana_jum_piesa == coloana - 1)):  # stanga jos
            return True
        return False


class Stare:
    """
    Clasa folosita de algoritmii minimax si alpha-beta
    Are ca proprietate tabla de joc
    Functioneaza cu conditia ca in cadrul clasei Joc sa fie definiti JMIN si JMAX (cei doi jucatori posibili)
    De asemenea cere ca in clasa Joc sa fie definita si o metoda numita mutari() care ofera lista cu configuratiile posibile in urma mutarii unui jucator
    """

    def __init__(self, tabla_joc, j_curent, adancime, parinte=None, estimare=None):
        self.tabla_joc = tabla_joc
        self.j_curent = j_curent

        # adancimea in arborele de stari
        self.adancime = adancime

        # estimarea favorabilitatii starii (daca e finala) sau al celei mai bune stari-fiice (pentru jucatorul curent)
        self.estimare = estimare

        # lista de mutari posibile din starea curenta
        self.mutari_posibile = []

        # cea mai buna mutare din lista de mutari posibile pentru jucatorul curent
        self.stare_aleasa = None

    def mutari(self):
        l_mutari = self.tabla_joc.mutari(self.j_curent)
        juc_opus = Joc.jucator_opus(self.j_curent)
        l_stari_mutari = [Stare(mutare, juc_opus, self.adancime - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari

    def __str__(self):
        sir = str(self.tabla_joc) + "(Juc curent: " + self.j_curent + ")"
        return sir


""" Algoritmul MinMax """

noduri_pt_mutare = []

def min_max(stare,tipestimare=1):

    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare
    else: #2
        if stare.adancime==0 or stare.tabla_joc.final() :
            stare.estimare=stare.tabla_joc.estimeaza_scor_2(stare.adancime)
            return stare

    # calculez toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # aplic algoritmul minimax pe toate mutarile posibile (calculand astfel subarborii lor)
    mutariCuEstimare = [min_max(mutare, tipestimare) for mutare in stare.mutari_posibile]
    global noduri_pt_mutare
    noduri_pt_mutare.append(len(mutariCuEstimare))

    if stare.j_curent == Joc.JMAX:
        # daca jucatorul e JMAX aleg starea-fiica cu estimarea maxima
        stare.stare_aleasa = max(mutariCuEstimare, key=lambda x: x.estimare)
    else:
        # daca jucatorul e JMIN aleg starea-fiica cu estimarea minima
        stare.stare_aleasa = min(mutariCuEstimare, key=lambda x: x.estimare)
    stare.estimare = stare.stare_aleasa.estimare
    return stare


def alpha_beta(alpha, beta, stare,tipestimare=1):
    if stare.adancime == 0 or stare.tabla_joc.final():
        stare.estimare = stare.tabla_joc.estimeaza_scor(stare.adancime)
        return stare
    else: #2
        if stare.adancime==0 or stare.tabla_joc.final() :
            stare.estimare=stare.tabla_joc.estimeaza_scor_2(stare.adancime)
            return stare

    if alpha > beta:
        return stare  # este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    global noduri_pt_mutare
    noduri_pt_mutare.append(len(stare.mutari_posibile))

    if stare.j_curent == Joc.JMAX:
        estimare_curenta = float('-inf')

        for mutare in stare.mutari_posibile:
            # calculeaza estimarea pentru starea noua, realizand subarborele
            stare_noua = alpha_beta(alpha, beta, mutare, tipestimare)

            if (estimare_curenta < stare_noua.estimare):
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare
            if (alpha < stare_noua.estimare):
                alpha = stare_noua.estimare
                if alpha >= beta:
                    break

    elif stare.j_curent == Joc.JMIN:
        estimare_curenta = float('inf')

        for mutare in stare.mutari_posibile:

            stare_noua = alpha_beta(alpha, beta, mutare, tipestimare)

            if (estimare_curenta > stare_noua.estimare):
                stare.stare_aleasa = stare_noua
                estimare_curenta = stare_noua.estimare

            if (beta > stare_noua.estimare):
                beta = stare_noua.estimare
                if alpha >= beta:
                    break
    stare.estimare = stare.stare_aleasa.estimare

    return stare


def afis_daca_final(stare_curenta):
    #afisari frumoase cu timpi si nebunii
    final = stare_curenta.tabla_joc.final()
    if (final):
        if (Joc.SCOR_X == Joc.SCOR_0):
            print("Remiza!")
        else:
            if Joc.SCOR_X > Joc.SCOR_0:
                print("A castigat x")
                Joc.CASTIGATOR = 'x'
            else:
                print("A castigat 0")
                Joc.CASTIGATOR = '0'
        stare_curenta.tabla_joc.deseneaza_grid()
        stare_curenta.tabla_joc.afiseaza_scor()
        return True

    return False

def afisare_statistici (tip_algoritm, stare_curenta, timp_total_joc, nr_mutari, timp_jucator, timp_pc):


    stare_curenta.tabla_joc.afiseaza_scor()

    if tip_algoritm == '1':
        print ("Rezultate cu algoritmul Minmax")
    else:
        print ("Rezultate cu algoritmul Alpha-Beta")
    if len(timp_pc):
        print("--------------------------------")
        print("Timpul minim de gandire pentru PC: {} milisecunde\nTimpul maxim de gandire pentru PC: {} milisecunde\nTimpul mediu de gandire pentru PC: {} milisecunde\nMediana timpului de gandire pentru PC: {} milisecunde" \
        .format(min(timp_pc), max(timp_pc), stats.mean(timp_pc), stats.median(timp_pc)))
    if len(timp_jucator):
        print("--------------------------------")
        print("Timpul minim de gandire pentru jucator: {} milisecunde\nTimpul maxim de gandire pentru jucator: {} milisecunde\nTimpul mediu de gandire pentru jucator: {} milisecunde\nMediana timpului de gandire pentru jucator: {} milisecunde" \
        .format(min(timp_jucator), max(timp_jucator), stats.mean(timp_jucator), stats.median(timp_jucator)))
    print("--------------------------------")
    print("Numar total mutari PC: {}\nNumar total mutari utilizator: {}".format(nr_mutari[1], nr_mutari[0]))

    global noduri_pt_mutare
    if len(noduri_pt_mutare):
        print("--------------------------------")
        print("Numarul minim de noduri generate: {}\nNumarul maxim de noduri generate: {}\nNumarul mediu de noduri generate: {}\nMediana numarului de noduri generate: {}" \
            .format(min(noduri_pt_mutare), max(noduri_pt_mutare), stats.mean(noduri_pt_mutare), stats.median(noduri_pt_mutare)))
    print("--------------------------------")
    print("Timpul total de joc: {}".format(timp_total_joc))

def main():
    # initializare algoritm
    raspuns_valid = False
    while not raspuns_valid:
        tip_algoritm = input("Algorimul folosit? (raspundeti cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")
        if tip_algoritm in ['1', '2']:
            raspuns_valid = True
        else:
            print("Nu ati ales o varianta corecta.")
    # initializare jucatori
    raspuns_valid = False
    while not raspuns_valid:
        Joc.JMIN = input("Doriti sa jucati cu x sau cu 0? ").lower()
        if (Joc.JMIN in ['x', '0']):
            raspuns_valid = True
        else:
            print("Raspunsul trebuie sa fie x sau 0.")

    while True:
        optiune = input ("Alegeti dificultatea la care vreti sa jucati(incepator = 1/Mediu = 2/avansat = 3): ")

        if optiune in ['1', '2', '3']:
            if optiune == '1':
                adancime = 1
            elif optiune == '2':
                adancime = 2
            else:
                adancime = 3
            break

    while True:
        t = input("Timp timeout joc (minute): ")
        try:
            TMAX = int(t)
            break
        except ValueError:
            print("Valoarea introdusa trebuia sa fie un numar intreg")

    print ("Apasati tasta ESC daca doriti sa opriti jocul")
    # tip_algoritm = '1'
    # Joc.JMIN = 'x'

    Joc.JMAX = '0' if Joc.JMIN == 'x' else 'x'

    # initializare tabla
    tabla_curenta = Joc()
    print("Tabla initiala")
    print(str(tabla_curenta))

    # creare stare initiala
    stare_curenta = Stare(tabla_curenta, 'x', adancime)

    # setari interf grafica
    pygame.init()
    pygame.display.set_caption('Oprian George - X si O')
    # dimensiunea ferestrei in pixeli
    ecran = pygame.display.set_mode(size=(509, 509))  # N *100+ N-1
    Joc.initializeaza(ecran)

    de_mutat = False
    tabla_curenta.deseneaza_grid()
    # pdb.set_trace()

    jum_piesa_plasata = False
    linie_jum_piesa = -1
    coloana_jum_piesa = -1

    timp_inceput_joc = time.time()
    timp_initial_jucator = time.time()

    timp_jucator = []
    timp_pc = []
    numar_mutari = [0, 0]

    while True:

        timp_curent = time.time()

        if (timp_curent - timp_inceput_joc) // 60 >= TMAX:
            print("\n###########################################")
            print("Timpul alocat jocului a expirat")
            timp_total_joc = time.time() - timp_inceput_joc
            afisare_statistici(tip_algoritm, stare_curenta, timp_total_joc, numar_mutari, timp_jucator, timp_pc)
            break

        if (stare_curenta.j_curent == Joc.JMIN):
            # muta jucatorul
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # inchide fereastra
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print("Jocul a fost intrerupt de utilizator")
                    pygame.quit()  # inchide fereastra
                    sys.exit()
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()  # coordonatele clickului
                    for np in range(len(Joc.celuleGrid)):

                        if Joc.celuleGrid[np].collidepoint(pos):
                            # verifica daca punctul cu coord pos se afla in dreptunghi(celula)
                            linie = np // 10
                            coloana = np % 10

                            if stare_curenta.tabla_joc.matr[np] == Joc.GOL:
                                if de_mutat:
                                    stare_curenta.tabla_joc.matr[de_mutat[0] * 10 + de_mutat[1]] = Joc.GOL
                                    # stare_curenta.tabla_joc.matr[de_mutat[0]* 3 +de_mutat[1]]=Joc.GOL
                                    de_mutat = False
                                # plasez simbolul pe "tabla de joc"
                                if jum_piesa_plasata is False and stare_curenta.tabla_joc.mutare_valida(linie, coloana):
                                    stare_curenta.tabla_joc.matr[linie * 10 + coloana] = Joc.JMIN
                                    linie_jum_piesa = linie
                                    coloana_jum_piesa = coloana
                                    stare_curenta.tabla_joc.l_jum1piesa = linie #colorez celula in care am plasat
                                    stare_curenta.tabla_joc.c_jum1piesa = coloana
                                    jum_piesa_plasata = True

                                elif jum_piesa_plasata is True \
                                        and stare_curenta.tabla_joc.pot_completa_placuta(linie_jum_piesa, coloana_jum_piesa,
                                                                               linie, coloana):
                                    stare_curenta.tabla_joc.matr[linie * 10 + coloana] = Joc.JMIN
                                    linie_jum_piesa = -1
                                    coloana_jum_piesa = -1
                                    stare_curenta.tabla_joc.l_jum1piesa = -1  # decolorez celula care cand am piesa completa
                                    stare_curenta.tabla_joc.c_jum1piesa = -1
                                    jum_piesa_plasata = False

                                    stare_curenta.tabla_joc.calculeaza_scor() #calculez scorul dupa ce am facut o mutare valida

                                    # afisarea starii jocului in urma mutarii utilizatorului

                                    print("\nTabla dupa mutarea jucatorului")
                                    print(str(stare_curenta))
                                    timp_curent = time.time()
                                    print ("Jucatorul a gandit " + str(timp_curent - timp_initial_jucator) + " secunde")
                                    timp_jucator.append(timp_curent - timp_initial_jucator)
                                    numar_mutari[0] += 1

                                    # testez daca jocul a ajuns intr-o stare finala
                                    # si afisez un mesaj corespunzator in caz ca da
                                    if (afis_daca_final(stare_curenta)):
                                        print("\n###########################################")
                                        print("Sfarsitul jocului")
                                        timp_total_joc = time.time() - timp_inceput_joc
                                        afisare_statistici(tip_algoritm, stare_curenta, timp_total_joc, numar_mutari, timp_jucator, timp_pc)
                                        break

                                    # S-a realizat o mutare. Schimb jucatorul cu cel opus
                                    stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)
                                stare_curenta.tabla_joc.deseneaza_grid()
                                stare_curenta.tabla_joc.afiseaza_scor()
                                

        # --------------------------------
        else:  # jucatorul e JMAX (calculatorul)
            # Mutare calculator
            print("muta calculatorul")
            # preiau timpul in milisecunde de dinainte de mutare

            t_inainte = int(round(time.time() * 1000))
            if tip_algoritm == '1':
                stare_actualizata = min_max(stare_curenta)
            else:  # tip_algoritm==2
                stare_actualizata = alpha_beta(-500, 500, stare_curenta)
            stare_curenta.tabla_joc = stare_actualizata.stare_aleasa.tabla_joc
            stare_curenta.tabla_joc.calculeaza_scor()
            print("Tabla dupa mutarea calculatorului")
            print(str(stare_curenta))


            stare_curenta.tabla_joc.deseneaza_grid()
            stare_curenta.tabla_joc.afiseaza_scor()
            # preiau timpul in milisecunde de dupa mutare
            t_dupa = int(round(time.time() * 1000))
            print("Calculatorul a \"gandit\" timp de " + str(t_dupa - t_inainte) + " milisecunde.")
            timp_pc.append(t_dupa - t_inainte)
            numar_mutari[1] += 1
            if (afis_daca_final(stare_curenta)):
                print("\n###########################################")
                print("Sfarsitul jocului")
                timp_total_joc = time.time() - timp_inceput_joc
                afisare_statistici(tip_algoritm, stare_curenta, timp_total_joc, numar_mutari, timp_jucator, timp_pc)
                break

            # # S-a realizat o mutare. Schimb jucatorul cu cel opus
            stare_curenta.j_curent = Joc.jucator_opus(stare_curenta.j_curent)
            print("muta jucatorul")
            timp_initial_jucator = time.time()


if __name__ == "__main__":
    main()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
