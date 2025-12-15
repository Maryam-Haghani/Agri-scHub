=================
Agriculture *sc*-Hub
=================

.. toctree::
   :maxdepth: 2
   :caption: Contents
   :numbered:

.. grid:: 1 2 2 4
   :gutter: 2

   .. grid-item::
      .. image:: images/scOMG.png
         :width: 100%

   .. grid-item::
      .. image:: images/scCoBench_scCoExpVis.png
         :width: 100%

   .. grid-item::
      .. image:: images/scPredGO.png
         :width: 100%

   .. grid-item::
      .. image:: images/sc3UTR.png
         :width: 100%

Methods Supported
----------------

1. **sc-Ortho-Marker groups (scOMG)** is a method for cross-species cell annotation in plants (Chau et al., 2025, *Nature Communications*).

2. **scCoBench** compared 10 methods for co-expression analysis in scRNA-seq data using GFP marker genes (Chau et al., 2025).  
   The companion tool cCoExpVis allows quick *online exploration* of co-expression matrices for user-provided single-cell data.

3. **scPredGO** used machine learning to predict GO annotation from single-cell expression data (Chinnareddy et al., 2025).

4. **sc3UTR** demonstrated that improved 3′UTR annotation substantially improved the read mapping results for 10x Genomic single-cell data (Kundu et al., 2025).

Availability
------------

These methods and tutorials will be provided in the Ag-sc-Hub.


.. grid:: 1 2 3 3
   :gutter: 2

   .. grid-item-card:: Installation :octicon:`plug;1em;`
      :link: api
      :link-type: doc

      New to *Ag-sc-Hub*? Check out the installation guide.

   .. grid-item-card:: User guide :octicon:`info;1em;`
      :link: usage
      :link-type: doc

      Learn how to run the supported methods and follow the tutorials.

   .. grid-item-card:: API reference :octicon:`book;1em;`
      :link: api
      :link-type: doc

      Detailed documentation of the Ag-sc-Hub API.

   .. grid-item-card:: Tutorials :octicon:`play;1em;`
      :link: usage
      :link-type: doc

      Walk through real-world applications of Ag-sc-Hub methods.

   .. grid-item-card:: Discussion :octicon:`megaphone;1em;`
      :link: https://www.discourse.org

      Need help? Reach out on the forum to get your questions answered!

   .. grid-item-card:: GitHub :octicon:`mark-github;1em;`
      :link: https://github.com/LiLabAtVT/PlantSingleCell

      Find a bug or want to contribute? Check out the repo for the latest updates.



.. toctree::

   usage
   api
