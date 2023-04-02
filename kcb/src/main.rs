#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}

#[get("/recipe")]
fn recipe() -> &'static str {
    "None!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index, recipe])
}