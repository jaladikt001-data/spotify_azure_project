class reusable:
    def dropColumns(self, df, columns): # self comes first
        df = df.drop(*columns)
        return df