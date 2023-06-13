export interface Recipe {
    id: string;
    url: string;
    title: string;
    steps: [string];
    ingredients: [string];
    source: string;
    prepTime: string;
    import_date: string;
}
