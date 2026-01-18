Składnia elementów dokumentu
===========================

Nagłówki tekstowe (poziomy 1-4)
--------------------------------

Poziom 1
========

Poziom 2
--------

Poziom 3
~~~~~~~~

Poziom 4
^^^^^^^^

Akapit tekstowy (treść)
-----------------------

To jest zwykły akapit tekstu. Możesz w nim pisać normalnie, w kilku liniach,  
Sphinx automatycznie łączy je w jeden blok.

Akapit informacyjny (Note, Tip)
--------------------------------

.. note::
   To jest akapit informacyjny typu Note.

.. tip::
   To jest akapit typu Tip.

Fragment kodu (liniowy, blokowy)
--------------------------------

Inline (liniowy): ``print("Hello World")``

Blokowy:

.. code-block:: python

   # To jest blok kodu
   for i in range(3):
       print(i)

Odnośniki (lokalny RtD, zewnętrzny)
-----------------------------------

- Lokalny: :doc:`autor`  
- Zewnętrzny: `Google <https://www.google.com>`_

Listy (numerowana, wypunktowana, definicji)
-------------------------------------------

- Lista wypunktowana
- Kolejny element
- Jeszcze jeden

1. Lista numerowana
2. Drugi element
3. Trzeci element

Terminy i definicje:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Termin
     - Definicja
   * - Python
     - Język programowania używany w tym projekcie
   * - RtD
     - Platforma do tworzenia dokumentacji

Obraz (z alternatywnym tekstem oraz podpisem)
--------------------------------------------

.. image:: picture.png
   :alt: Przykładowy obraz
   :width: 400px
   :align: center
   :caption: Podpis pod obrazkiem

Tabela (przykład)
-----------------

+-----------+-----------+
| Kolumna 1 | Kolumna 2 |
+===========+===========+
| Wiersz 1  | Dane      |
+-----------+-----------+
| Wiersz 2  | Dane      |
+-----------+-----------+
