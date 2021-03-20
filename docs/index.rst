Documentation
===================================

.. toctree::
   :maxdepth: 1

   autoapi/mal/index

Installation and Usage
===================================

To install the library: 

.. code-block::

   pip install -U mal-api


To import the library:

.. code-block:: python

   from mal import *

Examples
===================================

To call the API, you need to create an object.

**ID Query Example**

.. code-block:: python

   from mal import Anime
   anime = Anime(1)   # Cowboy Bebop
   print(anime.score) # prints 8.82
   anime.reload()     # reload object
   print(anime.score) # prints 8.81

**Search Query Example**

.. code-block:: python

   from mal import AnimeSearch
   search = AnimeSearch("cowboy bebop") # Search for "cowboy bebop"
   print(search.results[0].title)       # Get title of first result

Configuration
===================================

To configure timeout (default timeout is 5 seconds):

.. code-block:: python

   from mal import Anime
   from mal import config
   config.TIMEOUT = 1           # Import level config
   anime = Anime(1, timeout=1)  # Object level config
