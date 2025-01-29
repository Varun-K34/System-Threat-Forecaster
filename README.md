echo "## References" >> README.md
echo "1. [Pandas Documentation](https://pandas.pydata.org/docs)" >> README.md
echo "2. [Seaborn Documentation](https://seaborn.pydata.org)" >> README.md
echo "3. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)" >> README.md
echo "4. [Scikit-learn Documentation](https://scikit-learn.org/stable/)" >> README.md
echo "5. Online Tutorials & Research Papers (Towards Data Science, Analytics Vidhya, Kaggle)" >> README.md

# Stage and commit the changes
git add README.md
git commit -m "Added references to README"
git push origin main  # Change 'main' to your branch name if needed

