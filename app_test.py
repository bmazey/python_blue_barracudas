
def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()